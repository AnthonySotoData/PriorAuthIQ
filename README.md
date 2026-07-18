# PriorAuthIQ

<div align="center">

## Enterprise AI-Powered Prior Authorization Intelligence

> **🚧 Status:** MVP • Active Development

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

Instead of relying solely on a language model, PriorAuthIQ implements a **Retrieval-Augmented Generation (RAG)** architecture. Relevant policy content is retrieved from a vector database before OpenAI GPT-4.1-mini generates a structured response, improving factual accuracy and grounding every answer in source documentation.

The application automatically:

- Uploads payer policy PDFs
- Extracts and chunks policy text
- Generates semantic embeddings
- Stores documents in ChromaDB
- Retrieves relevant policy context
- Returns structured, citation-backed AI responses through a FastAPI REST API

---

## Why This Project?

Revenue cycle teams spend significant time manually reviewing payer policies to answer questions such as:

- Is prior authorization required?
- What documentation is required?
- What services are covered?
- What reimbursement rules apply?

PriorAuthIQ demonstrates how modern AI engineering techniques—including semantic search, vector databases, and AI-powered retrieval—can streamline this workflow while keeping responses grounded in the original policy documents.

---

## Features

### AI Pipeline

- Retrieval-Augmented Generation (RAG)
- Semantic search
- GPT-4.1-mini integration

### Knowledge Layer

- ChromaDB vector database
- PDF ingestion
- Automatic chunking and embeddings

### API

- FastAPI REST API
- Structured Pydantic responses
- Interactive Swagger documentation

### Quality

- Duplicate document replacement
- Automated testing with Pytest *(in progress)*

---

## System Architecture

PriorAuthIQ follows a modular Retrieval-Augmented Generation (RAG) architecture that ingests payer policy documents, indexes them into a vector database, retrieves relevant policy context, and generates structured, citation-backed responses using **OpenAI GPT-4.1-mini**.

<p align="center">
  <img
    src="images/priorauthiq-architecture.svg"
    alt="PriorAuthIQ Enterprise RAG Architecture"
    width="1000">
</p>

**Core workflow**

> Policy PDF → Text Extraction → Embeddings → ChromaDB → Semantic Retrieval → GPT-4.1-mini → Structured JSON Response

The diagram above illustrates the complete document ingestion, retrieval, and AI inference pipeline used to produce grounded responses from uploaded payer policy documentation.

---

## Repository Structure

The repository is organized into modular components that separate document ingestion, retrieval, AI inference, API endpoints, and supporting services.

```text
PriorAuthIQ/
├── src/
│   ├── api/                 # FastAPI REST API endpoints
│   ├── config/              # Application configuration and settings
│   ├── ingestion/           # PDF extraction and policy processing
│   ├── llm/                 # OpenAI provider and prompt orchestration
│   ├── models/              # Pydantic request and response schemas
│   ├── rag/                 # Retrieval pipeline and semantic search
│   ├── services/            # Business logic
│   └── utils/               # Shared utility functions
│
├── data/
│   ├── raw_policies/        # Original payer policy PDFs
│   ├── processed/           # Processed policy artifacts
│   ├── sample_policies/     # Sample documents for testing
│   └── vector_store/        # Persistent ChromaDB vector database
│
├── docs/                    # Project documentation
├── images/                  # README diagrams and assets
├── models/                  # Serialized model artifacts
├── notebooks/               # Research and experimentation
├── scripts/                 # Utility scripts
├── tests/                   # Automated test suite
│
├── README.md
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
└── .gitignore
```