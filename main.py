# main.py

import streamlit as st
from Home import show_home
from UploadPage import show_upload_page
from AskQuestionsPage import show_ask_questions_page

def render_sidebar():
    st.sidebar.title("LLM, VectorDb & LangChain")
    page = st.sidebar.radio("Navigoni në", ["Fillimi", "Insertimi i dokumentit", "Parashtrimi i pyetjeve"])
    return page

def main():
    st.set_page_config(page_title="LangChain & Qdrant App", layout="wide")
    page = render_sidebar()

    if page == "Fillimi":
        show_home()
    elif page == "Insertimi i dokumentit":
        show_upload_page()
    elif page == "Parashtrimi i pyetjeve":
        show_ask_questions_page()

if __name__ == "__main__":
    main()
