# UploadPage.py

import streamlit as st
from utils import get_vector_store
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings

def process_file(file):
    # Adjust this function based on the file types you support
    if file.type == "application/pdf":
        from PyPDF2 import PdfReader
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    else:
        return file.read().decode("utf-8")

def show_upload_page():
    st.title("Insertoni dokumentin tuaj")

    uploaded_file = st.file_uploader("Zgjedhni nje dokument...", type=["txt", "pdf"])
    if uploaded_file is not None:
        with st.spinner("Dokumenti po perpunohet..."):
            text_data = process_file(uploaded_file)

            # Split the text into chunks
            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_text(text_data)

            # Initialize vector store and embeddings
            vector_store = get_vector_store()
            embeddings = OpenAIEmbeddings()

            # Create embeddings and store them in Qdrant
            vector_store.add_texts(chunks, metadatas=[{"document_id": uploaded_file.name}] * len(chunks))

        st.success("Dokumenti u insertua dhe u ruajt me sukses!")

        # Navigate to Ask Questions page
        st.info("Tejkalimi ne fazen e parashtrimit te pyetjeve...")
        st.session_state.page = "Parashtrimi i pyetjeve"
        if st.button("Parashtrimi i pyetjeve"):
            st.session_state.page = "Parashtrimi i pyetjeve"
