# app/services/pinecone_client.py

import pinecone
from core.config import settings

pinecone.init(api_key=settings.PINECONE_API_KEY, environment=settings.PINECONE_ENV)

index = pinecone.Index(settings.INDEX_NAME)

def upsert_to_pinecone(vectors: list):
    """
    vectors: List of tuples (id, vector, metadata)
    """
    index.upsert(vectors=vectors)

def query_pinecone(vector: list, top_k=5):
    result = index.query(vector=vector, top_k=top_k, include_metadata=True)
    return result
