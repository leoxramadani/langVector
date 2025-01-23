import os
from dotenv import load_dotenv
import qdrant_client
from qdrant_client.http import models
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
from qdrant_client.http.exceptions import UnexpectedResponse
import pandas as pd
from typing import Union, List
from langchain.document_loaders import DataFrameLoader

load_dotenv()

def process_excel_file(file) -> str:
    """Process Excel file and convert it to text for vectorization"""
    df = pd.read_excel(file)
    
    # Convert DataFrame to string representation
    text_pieces = []
    
    # Add column headers
    headers = df.columns.tolist()
    text_pieces.append("Columns: " + ", ".join(headers))
    
    # Convert each row to a string representation
    for idx, row in df.iterrows():
        row_text = f"\nRow {idx + 1}:\n"
        for col in headers:
            row_text += f"{col}: {row[col]}\n"
        text_pieces.append(row_text)
    
    # Join all text pieces into a single string
    return "\n".join(text_pieces)

def calculate_excel_columns(df: pd.DataFrame, calculation_query: str) -> pd.DataFrame:
    """
    Perform calculations on Excel columns based on user query
    Example: "Calculate profit as revenue minus cost"
    """
    try:
        # Basic calculations mapping
        operations = {
            'sum': df.sum(),
            'average': df.mean(),
            'minimum': df.min(),
            'maximum': df.max(),
            'count': df.count()
        }
        
        # For now, just return basic statistics of numeric columns
        result_df = df.describe()
        return result_df
    except Exception as e:
        print(f"Error performing calculation: {str(e)}")
    return df

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
        vectors_config = models.VectorParams(
            size=1536,  # Set this to your desired vector size
            distance=models.Distance.COSINE  # Specify the distance metric
        )
        client.recreate_collection(collection_name=collection_name, vectors_config=vectors_config)

    embeddings = OpenAIEmbeddings()

    vector_store = Qdrant(
        client=client,
        collection_name=collection_name,
        embeddings=embeddings,
    )

    return vector_store


#this is it