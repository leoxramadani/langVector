import os
from dotenv import load_dotenv
import qdrant_client
from qdrant_client.http import models
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
from qdrant_client.http.exceptions import UnexpectedResponse

load_dotenv()

def get_vector_store():
    client = qdrant_client.QdrantClient(
        os.getenv("QDRANT_API_URL"),
        api_key=os.getenv("QDRANT_API_KEY")
    )

    collection_name = os.getenv("QDRANT_COLLECTION_NAME")

    # Check if the collection exists
    try:
        client.get_collection(collection_name)
        collection_exists = True
    except UnexpectedResponse:
        collection_exists = False

    # If the collection does not exist, create it
    if not collection_exists:
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE)
        )

    embeddings = OpenAIEmbeddings()

    vector_store = Qdrant(
        client=client,
        collection_name=collection_name,
        embeddings=embeddings,
    )

    return vector_store
