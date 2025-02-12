# main.py

import streamlit as st
from Home import show_home
from UploadPage import show_upload_page
from AskQuestionsPage import show_ask_questions_page

def render_sidebar():

    st.sidebar.markdown(
            """
            <style>
            @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css');
            </style>
            """, unsafe_allow_html=True
        )

    st.sidebar.title("LLM, VectorDb & LangChain")
    page = st.sidebar.radio("Navigoni në", ["Hyrja", "Insertimi i dokumenteve", "Pyetni sistemin"])

    st.sidebar.markdown(
            """
            <hr style="margin-top: 30px; margin-bottom: 10px;background:red;margin-top:400px;">
            <p style="text-align:center">
                <i class="fa fa-user" style="font-size:20px; margin-right:8px;"></i> Leotrim Ramadani
            </p>
            """, unsafe_allow_html=True
    )

    return page

def main():
    st.set_page_config(page_title="LangChain & Qdrant App", layout="wide")
    page = render_sidebar()

    if page == "Hyrja":
        show_home()
    elif page == "Insertimi i dokumenteve":
        show_upload_page()
    elif page == "Pyetni sistemin":
        show_ask_questions_page()

if __name__ == "__main__":
    main()
