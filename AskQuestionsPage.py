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
        "Çfare lloj pyetje dëshironi të bëni?",
        ["Pyetje të përgjithshme", "Prezantim i një Excel dokumenti"]
    )

    user_question = st.text_input("Pyetja juaj:")

    if user_question:
        with st.spinner("Procesimi i pyetjes tuaj..."):
            if question_type == "Prezantim i një Excel dokumenti" and 'current_df' in st.session_state:
                # Handle Excel calculations
                df = st.session_state['current_df']
                result_df = calculate_excel_columns(df, user_question)
                st.write("### Rezulati:")
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
                st.write("### Pergjigja:")
                st.write(response)