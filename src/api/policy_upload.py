from pathlib import Path
from tempfile import NamedTemporaryFile
from uuid import uuid4

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from src.ingestion.document_processor import process_policy_document
from src.models.schemas import PolicyUploadResponse
from src.rag.vector_store import (
    delete_policy_document,
    index_policy_chunks,
)


router = APIRouter(
    prefix="/policies",
    tags=["Policy Upload"],
)


@router.post(
    "/upload",
    response_model=PolicyUploadResponse,
)
async def upload_policy(
    file: UploadFile = File(...),
    payer: str = Form(...),
    policy_title: str = Form(...),
) -> PolicyUploadResponse:
    """
    Upload, process, and index a payer policy PDF.

    Re-uploading the same payer, policy title, and filename replaces the
    previously indexed copy instead of creating duplicate chunks.
    """

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported.",
        )

    normalized_payer = payer.strip()
    normalized_policy_title = policy_title.strip()

    if not normalized_payer:
        raise HTTPException(
            status_code=400,
            detail="Payer is required.",
        )

    if not normalized_policy_title:
        raise HTTPException(
            status_code=400,
            detail="Policy title is required.",
        )

    file_bytes = await file.read()

    if not file_bytes:
        raise HTTPException(
            status_code=400,
            detail="The uploaded PDF is empty.",
        )

    document_id = str(uuid4())
    source_file = file.filename or f"{document_id}.pdf"

    temporary_path: Path | None = None

    try:
        with NamedTemporaryFile(
            suffix=".pdf",
            delete=False,
        ) as temporary_file:
            temporary_file.write(file_bytes)
            temporary_path = Path(temporary_file.name)

        chunks = process_policy_document(
            pdf_path=str(temporary_path),
            payer=normalized_payer,
            policy_title=normalized_policy_title,
        )

        if not chunks:
            raise HTTPException(
                status_code=400,
                detail="No readable text was found in the uploaded PDF.",
            )

        for chunk in chunks:
            chunk["source_file"] = source_file

        delete_policy_document(
            payer=normalized_payer,
            policy_title=normalized_policy_title,
            source_file=source_file,
        )

        chunks_indexed = index_policy_chunks(
            chunks=chunks,
            document_id=document_id,
        )

        return PolicyUploadResponse(
            message="Policy indexed successfully.",
            document_id=document_id,
            payer=normalized_payer,
            policy_title=normalized_policy_title,
            source_file=source_file,
            chunks_indexed=chunks_indexed,
        )

    except HTTPException:
        raise

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process policy: {exc}",
        ) from exc

    finally:
        if temporary_path and temporary_path.exists():
            temporary_path.unlink()