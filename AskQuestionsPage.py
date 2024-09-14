# AskQuestionsPage.py

import streamlit as st
from utils import get_vector_store
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def show_ask_questions_page():
    st.title("Parashtrimi i pyetjeve per dokumentin tuaj")

    vector_store = get_vector_store()

    user_question = st.text_input("Pyetja juaj:")

    if user_question:
        with st.spinner("Ne kerkim te pergjigjes..."):
            # Set up the retrieval-based QA chain
            llm = OpenAI()
            qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
            )

            # Run the question through the QA chain
            response = qa_chain.run(user_question)

        st.write("### Pergjigja:")
        st.write(response)
