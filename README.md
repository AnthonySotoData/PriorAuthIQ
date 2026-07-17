# PriorAuthIQ

<div align="center">

### Enterprise AI-Powered Prior Authorization Intelligence Platform

Transform payer policy documents into structured, citation-backed prior authorization intelligence using **Retrieval-Augmented Generation (RAG)**, semantic search, vector embeddings, and Large Language Models.

---

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1--mini-412991?logo=openai)
![ChromaDB](https://img.shields.io/badge/Vector%20Database-ChromaDB-orange)
![Sentence Transformers](https://img.shields.io/badge/Embeddings-SentenceTransformers-red)
![RAG](https://img.shields.io/badge/Architecture-RAG-success)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

# Overview

PriorAuthIQ is an AI-powered healthcare intelligence platform designed to assist revenue cycle teams with interpreting payer policies related to prior authorization, reimbursement, and coverage requirements.

Rather than relying solely on a large language model, PriorAuthIQ implements a Retrieval-Augmented Generation (RAG) architecture that retrieves relevant policy content from a vector database before generating a structured response. This approach improves factual accuracy, reduces hallucinations, and grounds every answer in the underlying policy document.

The platform automatically ingests payer policy PDFs, extracts and chunks text, generates semantic embeddings, stores them in ChromaDB, and uses OpenAI GPT-4.1-mini to generate citation-backed responses through a FastAPI REST API.

---

# Why PriorAuthIQ?

Healthcare organizations spend thousands of hours each year manually reviewing payer policies to answer questions such as:

- Is prior authorization required?
- What documentation is required?
- What are the reimbursement requirements?
- What coverage limitations exist?

PriorAuthIQ demonstrates how modern AI techniques—including semantic search, vector databases, and Retrieval-Augmented Generation—can accelerate policy review while maintaining transparency through citation-backed responses.

---

# Key Features

- AI-powered payer policy interpretation
- Retrieval-Augmented Generation (RAG)
- Semantic search using Sentence Transformers
- ChromaDB vector database
- OpenAI GPT-4.1-mini integration
- PDF upload and automatic policy ingestion
- Structured Pydantic responses
- Citation-backed answers
- Duplicate document replacement
- FastAPI REST API
- Interactive Swagger documentation

---

> **Current Status:** Active development — MVP nearly complete.