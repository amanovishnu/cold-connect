import pandas as pd
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(clean_text):

    st.title(
            "📧 Outreach Composer for Job Search",
            help="Simple Streamlit for Generating Cold emails/Messages text for Job search"
    )
    try:
        api_key = st.sidebar.text_input(
            label="Step 1: Groq API Key",
            placeholder="Enter your groq api Key",
            help="Enter your GROQ API Key",
            value="",
            type="password"
        )

        upload_file = st.sidebar.file_uploader("Step 2: Choose a file")
        if upload_file:
            df = pd.read_csv(upload_file)
            portfolio = Portfolio(file_path=df)

        username = st.sidebar.text_input(
            label="Step 3: Enter your name",
            placeholder="Enter your name",
            help="Enter your name to be embedded in the response [default: John Doe]"
        )
        referrer_name = st.sidebar.text_input(
            label="Step 4: Enter referrer name",
            placeholder="Enter the name of the referrer",
            help="Enter the name of the referrer to be embedded in the response [default: Jane Doe]"
        )
        message_type = st.sidebar.radio(
            label="Step 5: What do you want to generate?",
            options=["e-mail", "linkedin-message"],
            help="Choose the type of message you want to generate"
        )
        model_selector = st.sidebar.selectbox(
            label="Step 6: Choose a model",
            options=["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "llama3-70b-8192", "gemma2-9b-it"],
            placeholder="choose a model",
            help="Choose a model to generate the text [default: llama-3.3-70b-versatile]"
        )
        temperature = st.sidebar.slider(
            label="Step 7: Creativity",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.1,
            help="How creative the model should be in generating the text 0 (is less creative) 1 (is more creative)"
        )

        llm = Chain(
            api_key=api_key,
            temperature=temperature,
            model_name=model_selector,
        )

        st.markdown(
            """
            **Note:** On the first run, the app will download the **all-MiniLM-L6-v2** model from Hugging Face. 
            This may cause a delay of a few minutes.
            """
        )

        url_input = st.text_input(
            label="Paste the URL:",
            placeholder="Paste the URL of the job posting"
        )
        submit_button = st.button("Generate", icon="✉️")

        if "response_history" not in st.session_state:
            st.session_state.response_history = []

        if submit_button:
            try:
                loader = WebBaseLoader([url_input]).load()
                data = clean_text(loader.pop().page_content)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)
                for job in jobs:
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links, username, referrer_name, message_type)
                    st.code(email, language='markdown', wrap_lines=True)
                    st.session_state.response_history.insert(0, email)
            except Exception as e:
                st.error(f"An Error Occurred: {e}")

        with st.expander("Response History", icon="📧"):
            for response in st.session_state.response_history:
                st.code(response, language='markdown', wrap_lines=True)
        if upload_file:
            with st.expander("Click here to view uploaded file", icon="📧"):
                st.dataframe(df, use_container_width=True)
    except Exception:
        st.warning("Please fill in the required fields in the sidebar to generate the response message") 


if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Outreach Composer for Job Search", page_icon="📧")
    create_streamlit_app(clean_text)

