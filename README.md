# PriorAuthIQ

<div align="center">

## Enterprise AI-Powered Prior Authorization Intelligence

**Transform payer policy documents into structured, citation-backed prior authorization intelligence using Retrieval-Augmented Generation (RAG), semantic search, vector embeddings, and Large Language Models.**

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1--mini-412991?logo=openai)
![ChromaDB](https://img.shields.io/badge/Vector%20Database-ChromaDB-orange)
![Sentence Transformers](https://img.shields.io/badge/Embeddings-SentenceTransformers-red)
![RAG](https://img.shields.io/badge/Architecture-RAG-success)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

## Overview

PriorAuthIQ is an AI-powered healthcare intelligence platform that helps interpret insurance payer policies related to prior authorization, reimbursement, and coverage requirements.

Instead of relying solely on a language model, PriorAuthIQ implements a **Retrieval-Augmented Generation (RAG)** architecture. Relevant policy content is retrieved from a vector database before an LLM generates a structured response, improving factual accuracy and grounding every answer in source documentation.

The application automatically:

- Uploads payer policy PDFs
- Extracts and chunks policy text
- Generates semantic embeddings
- Stores documents in ChromaDB
- Retrieves relevant policy context
- Produces structured, citation-backed AI responses through a FastAPI REST API

---

## Why This Project?

Revenue cycle teams spend significant time manually reviewing payer policies to answer questions such as:

- Is prior authorization required?
- What documentation is required?
- What services are covered?
- What reimbursement rules apply?

PriorAuthIQ demonstrates how modern AI engineering techniques—including semantic search, vector databases, and Retrieval-Augmented Generation—can streamline this workflow while keeping responses grounded in the original policy documents.

---

## Current Features

- ✅ Retrieval-Augmented Generation (RAG)
- ✅ OpenAI GPT-4.1-mini integration
- ✅ Semantic search with Sentence Transformers
- ✅ ChromaDB vector database
- ✅ PDF upload and automatic policy ingestion
- ✅ Citation-backed responses
- ✅ Structured Pydantic outputs
- ✅ Duplicate document replacement
- ✅ FastAPI REST API
- ✅ Interactive Swagger documentation
- ✅ Automated testing with Pytest *(in progress)*

---

> **Status:** Active development — MVP nearing completion.