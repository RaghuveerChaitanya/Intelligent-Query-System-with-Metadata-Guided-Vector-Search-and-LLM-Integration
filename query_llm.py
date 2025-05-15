import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue
from openai import OpenAI

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Init OpenAI client
openai = OpenAI(api_key=OPENAI_API_KEY)

# Load model & Qdrant
model = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient(host="localhost", port=6333)
collection_name = "people_info"

def search_vector_db(query, user_id):
    vector = model.encode(query).tolist()
    results = client.search(
    collection_name=collection_name,
    query_vector=vector,
    limit=3,
    query_filter=Filter(
        must=[
            FieldCondition(
                key="user_id", match=MatchValue(value=user_id)
                )
            ]
        )
    )

    return [hit.payload['text'] for hit in results]

def generate_response(query, context):
    prompt = f"""You are an assistant. Use the context below to answer the question.
    
Context:
{context}

Question: {query}
"""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    query = input("Enter your question: ")
    user_id = input("Enter your user_id (e.g. john123): ")

    context_data = search_vector_db(query, user_id)
    context = "\n".join(context_data)

    final_answer = generate_response(query, context)
    print("\nAnswer:\n", final_answer)
