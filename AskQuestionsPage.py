# AskQuestionsPage.py

import streamlit as st
from utils import get_vector_store
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from utils import calculate_excel_columns

def show_ask_questions_page():
    st.title("Make question about your document")
    #st.title("Parashtrimi i pyetjeve per dokumentin tuaj")


    vector_store = get_vector_store()

    question_type = st.radio(
        "What type of question do you want to ask?",
        ["General Question", "Excel presentation"]
    )

    user_question = st.text_input("Your question:")
    #user_question = st.text_input("Pyetja juaj:")

    if user_question:
        with st.spinner("Processing your request..."):
            if question_type == "Excel presentation" and 'current_df' in st.session_state:
                # Handle Excel calculations
                df = st.session_state['current_df']
                result_df = calculate_excel_columns(df, user_question)
                st.write("### Result:")
                st.dataframe(result_df)
            else:
                # Handle general questions using QA chain
                llm = OpenAI()
                qa_chain = RetrievalQA.from_chain_type(
                    llm=llm,
                    chain_type="stuff",
                    retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
                )
                response = qa_chain.run(user_question)
                st.write("### Answer:")
                st.write(response)