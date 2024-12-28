# outreach-composer-for-job-search

**`outreach-composer-for-job-search`** is a Streamlit application designed to help job seekers generate personalized cold emails or LinkedIn messages. By leveraging the **`groq-api`** and various language models, the app extracts job postings from provided URLs, cleans the text, and crafts professional outreach messages.

### Features
- Extract job postings directly from career pages.
- Create personalized cold emails or LinkedIn messages.
- Tailor messages with user and referrer details.
- Integrate relevant portfolio links into the messages.
- Offer support for multiple language models and adjustable creativity levels.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/amanovishnu/outreach-composer-for-job-search.git
    cd outreach-composer-for-job-search
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your browser and navigate to **`http://localhost:8501`**.

3. Follow the steps in the sidebar to generate your personalized outreach messages:
    - Input your Groq API Key.
    - Upload your portfolio CSV file.
    - Provide your name and the referrer’s name.
    - Select the message type (email or LinkedIn message).
    - Choose a language model and adjust the creativity level.
    - Paste the job posting URL and click **"Generate"**.

### File Structure

- **`app.py`** : Main Streamlit application file
- **`chains.py`** : Contains the Chain class for extracting jobs and generating messages
- **`portfolio.py`** : Contains the Portfolio class for managing and querying portfolio links
- **`utils.py`** : Utility functions for cleaning text and fetching model lists
- **`notebook.ipynb`** : Jupyter notebook for testing and development
- **`docker-compose.yml`** : Docker Compose configuration (empty)
- **`Dockerfile`** : Dockerfile for containerizing the application (empty)
- **`.env`** : Environment variables file (not included in the repository)
- **`.gitignore`** : Git ignore file
- **`LICENSE`** : License file
- **`README.md`** : Project README file
- **`setup.cfg`** : Configuration for flake8 and mypy
- **`settings.json`** : VSCode settings

### License
This project is licensed under the MIT License. See the **LICENSE** file for details.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Groq API](https://groq.com/)
- [LangChain](https://langchain.com/)

### Contact
For any questions or inquiries, please contact [geekymano@gmail.com](mailto:geekymano@gmail.com).