FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV USER_AGENT="outreach-composer-for-job-search"
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]