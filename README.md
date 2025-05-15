# Intelligent-Query-System-with-Metadata-Guided-Vector-Search-and-LLM-Integration
 ## [DPR - Detailed Project Report]Goal of the Project:

  ask a question → LLM reads it → Pulls data from a vector database like Qdrant or 
 pgvector → Filters based on user_id → Returns an enriched answer.

"Build a system where a user enters a query. That query is passed to an LLM (like ChatGPT), 
which uses relevant context from a vector database (Qdrant) to answer intelligently. 
The vector DB search is filtered by user ID."

1. You enter a query + user ID

       |
2. Query is converted into an embedding (vector)

       |
3. Vector is searched in Qdrant with metadata filter (user_id)

       |
4. Top 3 relevant documents are retrieved

       |
5. Query + context is passed to ChatGPT (LLM)

       |
6. ChatGPT generates a smart response
  
       |
7. Response is shown to the user

“I’ve built a system using Python + Qdrant + OpenAI where a query is passed to an LLM, 
but before that, I reduce its search space using vector search filtered by user ID. 
I encode personal data into vectors using Sentence Transformers, store them in Qdrant, and then retrieve top matches and pass that as context to the LLM for intelligent response generation.”

Concepts I have Learned & Used:
| Concept                  | I Used It In                            |
| ------------------------ | --------------------------------------- |
| Vector DB                | Qdrant (store and search semantic data) |
| Embedding Models         | Sentence Transformers (for vectorizing) |
| Metadata Filtering       | Qdrant user_id filtering                |
| LLM                      | OpenAI GPT-3.5                          |
| Prompt Engineering       | Custom prompt with query + context      |
| Function Calling Concept | Manually sending retrieved data to LLM  |
| Python Libraries         | `qdrant-client`, `openai`, `dotenv`     |


Project steps how I did.

 here I used:

-Qdrant (vector DB)

-OpenAI LLM

-Python (with FastAPI for simplicity later)

-Sentence Transformers to embed text

-Metadata filtering (like user_id)

| Requirements          | Tool                  |
| --------------------- | --------------------- |
| Code Editor           | VS Code               |
| Embeddings            | Sentence Transformers |
| Vector Database       | Qdrant (Docker)       |
| LLM                   | OpenAI GPT            |
| Programming Language  | Python                |
| Environment Variables | dotenv                |


STEP 1: Install Requirements
    pip install openai qdrant-client sentence-transformers python-dotenv

Step 2: Create a Virtual Environment (Recommended)
    python -m venv venv
    
    venv\Scripts\activate

Step 3: Install Dependencies
    pip install -r requirements.txt

Step 4: Start Qdrant (in a separate terminal window)
    docker run -p 6333:6333 qdrant/qdrant

 Step 5: Run the Python Files
 Ingest data (into Qdrant):
    python ingest_data.py
 Ask questions (goes to OpenAI and uses filtered context):
    python query_llm.py

    Enter your question: What does John do?
    Enter your user_id (e.g. john123): john123

Answer: John is a backend engineer specializing in microservices. He builds APIs with Python and FastAPI.

    Enter your question: What does Jane do?
    Enter your user_id: jane456

Answer: Jane is a data scientist who loves ML and analytics. She works with big data tools like Spark and Airflow.
