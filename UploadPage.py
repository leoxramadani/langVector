# UploadPage.py

import streamlit as st
from utils import get_vector_store
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from utils import process_excel_file
from utils import pd
from utils import get_vector_store, process_excel_file
import pandas as pd
def process_file(file):
    # Adjust this function based on the file types you support
    if file.type == "application/pdf":
        from PyPDF2 import PdfReader
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
            print(f"Extracted Text: {text[:500]}")
        return text
    else:
        return file.read().decode("utf-8")

def show_upload_page():
    st.title("Shtoni një dokument")

    uploaded_file = st.file_uploader(
        "Zgjedhni dokumentin tuaj...", 
        type=["txt", "pdf", "xlsx", "xls"]
    )

    if uploaded_file is not None:
        with st.spinner("Dokumenti juaj po procesohet..."):
            try:
                # Process based on file type
                if uploaded_file.type in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/vnd.ms-excel"]:
                    # Preview Excel data first
                    df = pd.read_excel(uploaded_file)
                    st.write("Prezantimi i të dhënave nga Excel:")
                    st.dataframe(df.head())
                    
                    # Store DataFrame in session state for later use
                    st.session_state['current_df'] = df
                    
                    # Process the file for vectorization
                    text_data = process_excel_file(uploaded_file)
                else:
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

                # Create embeddings and store them
                metadata = [{"document_id": uploaded_file.name}] * len(chunks)
                result = vector_store.add_texts(chunks, metadatas=metadata)

                st.success("Dokumenti juaj është regjistruar me sukses!")
                st.info("Kalimi në hapin tjeter...")

                if st.button("Faza e pyetjeve"):
                    st.session_state.page = "Pyetni sistemin"
                    
            except Exception as e:
                st.error(f"Probleme me procesimin e dokumentit: {str(e)}")
                st.info("Please make sure your Excel file is properly formatted and try again.")