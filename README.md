# Multi-Modal RAG & Intelligent Document Processing System

## Overview

This project is a Multi-Modal Retrieval-Augmented Generation (RAG) and Intelligent Document Processing (IDP) system built using Python, Large Language Models (LLMs), embeddings, and vector databases.

The system can:

* Extract data from multiple document formats
* Convert text into embeddings
* Store embeddings in a vector database
* Retrieve relevant information using semantic search
* Rewrite user queries using an LLM
* Generate intelligent responses using retrieved context
* Support future multimodal extensions such as images, audio, and OCR

---

# Project Architecture

```text
User Query
    ↓
Query Rewriting (LLM)
    ↓
Embedding Generation
    ↓
Vector Database Retrieval
    ↓
Relevant Context Retrieval
    ↓
Final LLM Response
```

---

# Features

## Document Processing

Supports:

* PDF files
* DOCX files
* TXT files
* Source code files
* Future support for images/audio

---

## Query Rewriting

Uses an LLM to:

* Correct spelling mistakes
* Correct grammar mistakes
* Expand short queries
* Improve semantic retrieval

Example:

```text
Input:
wher tajmahal locatd

Output:
Where is the Taj Mahal located?
```

---

## Embedding Generation

Converts text into vector representations using:

* sentence-transformers
* all-MiniLM-L6-v2

---

## Vector Database

Stores embeddings for semantic search.

Supported databases:

* ChromaDB
* Pinecone
* FAISS
* Weaviate

---

## Semantic Search

Retrieves relevant chunks using:

* cosine similarity
* vector similarity search
* semantic retrieval

---

# Technologies Used

## Backend

* Python
* FastAPI (future integration)
* Flask (optional)

---

## AI/ML

* Sentence Transformers
* LangChain
* LLM APIs
* RAG Architecture

---

## LLM Providers

* Groq
* OpenAI
* Gemini
* Llama Models

---

## Vector Databases

* Pinecone
* ChromaDB

---

# Project Structure

```text
genai/
│
├── data_related_methods/
│   ├── __init__.py
│   ├── data_extract.py
│   ├── data_chunks.py
│   ├── data_to_embeddings.py
│
├── query_processing/
│   ├── __init__.py
│   ├── query_rewriter.py
│
├── vector_db/
│   ├── __init__.py
│   ├── pinecone_storage.py
│   ├── data_retrieval.py
│
├── Data/
│   ├── sample.pdf
│   ├── sample.docx
│
├── api_keys.env
├── requirements.txt
├── README.md
```

---

# Installation

## Clone Repository

```bash
git clone <repository_url>
cd genai
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Required Packages

```bash
pip install sentence-transformers
pip install langchain
pip install langchain-community
pip install pypdf
pip install python-docx
pip install pinecone
pip install chromadb
pip install groq
pip install python-dotenv
```

---

# Environment Variables

Create:

```text
api_keys.env
```

Example:

```text
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

---

# Document Extraction

Example:

```python
from data_related_methods.data_extract import extract_text

text = extract_text(r"Data/sample.pdf")

print(text)
```

---

# Embedding Generation

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embedding = model.encode(
    "What is Artificial Intelligence?"
)
```

---

# Query Rewriting Example

```python
from query_processing.query_rewriter import rewrite_query

query = "wher tajmahal locatd"

rewritten_query = rewrite_query(query)

print(rewritten_query)
```

---

# Vector Search Flow

```python
query
↓
embedding generation
↓
vector similarity search
↓
top-k relevant chunks
↓
final llm response
```

---

# Retrieval-Augmented Generation (RAG)

RAG combines:

* semantic retrieval
* embeddings
* vector databases
* LLM reasoning

This allows the model to answer questions using custom uploaded documents.

---

# Future Improvements

## Planned Features

* OCR support
* Audio transcription
* Image understanding
* Hybrid search
* Reranking
* Conversational memory
* Streaming responses
* FastAPI deployment
* React frontend
* Multi-user authentication

---

# Example Use Cases

* AI Document Assistant
* Resume Analyzer
* Enterprise Knowledge Base
* Legal Document Search
* Medical Report QA
* Educational Chatbot
* Multi-modal AI Assistant

---

# Important Concepts Used

## Embeddings

Convert text into vectors.

---

## Vector Database

Stores embeddings for semantic retrieval.

---

## Query Rewriting

Improves user queries before retrieval.

---

## Semantic Search

Finds meaning-based matches instead of exact keywords.

---

## Chunking

Splits large documents into smaller searchable pieces.

---

# Author

A Yaswanth Reddy

Skills:

* LLMs
* RAG Systems
* LangChain
* Python
* Vector Databases
* Multi-modal AI
* Semantic Search

---

# License

This project is for educational and research purposes.
