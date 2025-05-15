import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct

load_dotenv()
model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(host="localhost", port=6333)

collection_name = "people_info"
client.recreate_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

data = [
    {"id": 1, "user_id": "john123", "text": "John is a backend engineer specializing in microservices."},
    {"id": 2, "user_id": "john123", "text": "He builds APIs with Python and FastAPI."},
    {"id": 3, "user_id": "jane456", "text": "Jane is a data scientist who loves ML and analytics."},
    {"id": 4, "user_id": "jane456", "text": "She works with big data tools like Spark and Airflow."}
]

points = []
for item in data:
    embedding = model.encode(item["text"]).tolist()
    points.append(
        PointStruct(
            id=item["id"],
            vector=embedding,
            payload={"user_id": item["user_id"], "text": item["text"]}
        )
    )

client.upsert(collection_name=collection_name, points=points)
print("Data ingested into Qdrant!")
      