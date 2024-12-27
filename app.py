import streamlit as st
import pandas as pd

st.set_page_config(page_title="cold-email-generator", page_icon="📬", layout="wide")
st.title("📬 cold-email-generator")

with st.sidebar:
    upload_groq_api_key = st.text_input(
        label="enter groq api key",
        placeholder="enter groq api key",
        type="password",
        help="Enter the api key for the application to work"
    )
    if upload_groq_api_key:
        choose_model = st.selectbox(
            label="choose a model",
            options=[
                'llama-3.1-8b-instant', 'llama-3.3-70b-versatile',
                'llama3-8b-8192', 'mixtral-8x7b-32768',
                'gemma2-9b-it'
            ],
            help="Choose a model to generate email"
        )
    else:
        st.info("Please enter your Groq API key to choose a model.")

    upload_excel = st.file_uploader(
        label="upload file",
        type=["csv", "xlsx"],
        help="Select a CSV or Excel file"
    )


input_url = st.text_input(label="Enter Job URL", placeholder="Enter Job URL")
submit_btn = st.button(label="Generate Email")

if upload_excel:
    df = pd.read_csv(upload_excel)
    st.write(df, use_container_width=True)

if submit_btn:
    st.code(input_url, language="markdown")