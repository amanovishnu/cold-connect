FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV USER_AGENT="cold-connect"
RUN python -c "import chromadb; chromadb.Client().get_or_create_collection('my_collection')._embed('sample text')"
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]