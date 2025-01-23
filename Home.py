# Home.py

import streamlit as st

def show_home():
    st.title("Large Language Models, Langchain, VectorDB")
    st.write("""
    **Large Language Models**
    - Një **LLM** është një program kompjuterik që është ushqyer me mjaft shembuj për të qenë në gjendje të njohë dhe interpretojë gjuhën njerëzore ose lloje të tjera të të dhënave komplekse. Shumë **LLM** trajnohen me të dhëna të mbledhura nga Interneti — mijëra ose miliona gigabajtë tekst. Por cilësia e shembujve ndikon në mënyrën se si **LLM** do të mësojë gjuhën natyrore, kështu që programuesit e një **LLM** mund të përdorin një grup të dhënash më të kuruar.

    **Langchain**
    - **LangChain** është një kornizë me burim të hapur për ndërtimin e aplikacioneve të bazuara në modele të mëdha gjuhësore (LLMs). LLM-të janë modele të mëdha të të mësuarit të thellë, të trajnuara paraprakisht me sasi të mëdha të dhënash, që mund të gjenerojnë përgjigje ndaj pyetjeve të përdoruesve—për shembull, të përgjigjen pyetjeve ose të krijojnë imazhe nga komandat e bazuara në tekst. **LangChain** ofron mjete dhe abstraksione për të përmirësuar personalizimin, saktësinë dhe rëndësinë e informacionit që gjenerojnë modelet. Për shembull, zhvilluesit mund të përdorin komponentët e **LangChain** për të ndërtuar zinxhirë të rinj komandash ose për të personalizuar shabllonet ekzistuese. **LangChain** gjithashtu përfshin komponentë që i lejojnë LLM-të të aksesojnë grupe të reja të dhënash pa ri-trajnim.
    
    **VectorDB**
    - Një bazë të dhënash me vektor ruan, menaxhon dhe indekson të dhëna vektorësh me përmasa të larta. Pikat e të dhënave ruhen si vargje numrash të quajtura **"vektorë,"** të cilat grupohen bazuar në ngjashmërinë e tyre. Ky dizajn mundëson pyetje me vonesë të ulët, duke e bërë atë ideal për aplikacionet e **AI**. Ndryshe nga bazat e të dhënave tradicionale relacionale me rreshta dhe kolona, pikat e të dhënave në një bazë të dhënash me **vektorë** përfaqësohen nga vektorë me një numër të caktuar përmasash. Për shkak se përdorin ngulitje vektorësh me përmasa të larta, bazat e të dhënave me vektorë janë më të afta për të trajtuar grupe të dhënash të pastrukturuara.  
    """)
