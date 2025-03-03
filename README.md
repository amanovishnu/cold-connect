# cold-connect

**`cold-connect`** is a Streamlit application designed to help job seekers generate personalized cold emails or LinkedIn messages. By leveraging the **`groq-api`** and various language models, the app extracts job postings from provided URLs, cleans the text, and crafts professional outreach messages.

### Features
- Extract job postings directly from career pages.
- Create personalized cold emails or LinkedIn messages.
- Tailor messages with user and referrer details.
- Integrate relevant portfolio links into the messages.
- Offer support for multiple language models and adjustable creativity levels.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/amanovishnu/cold-connect.git
    cd cold-connect
    ```

2. Create a virtual environment using Anaconda or `virtualenv`:

    **Using Anaconda:**
    ```sh
    conda create -n cenv python=3.13 -y
    conda activate cenv
    ```

    **Using `virtualenv`:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
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

**Note:** The first time you run the application, downloading the embedding model may take 2-3 minutes.

### Getting Groq API Key

1. Visit the [Groq API website](https://groq.com/).
2. Sign up for a free account.
3. Navigate to the API section and generate a new API key.
4. Copy the API key and use it in the application when prompted.


### Docker

##### Build and Run Locally

To create and run the Docker image:

1. Build the Docker image:
    ```sh
    docker build -t cold-connect .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8501:8501 cold-connect
    ```

3. Open your browser and navigate to **`http://localhost:8501`**.

##### Run with Pre-Built Image

A pre-built Docker image is available on Docker Hub:

1. Pull the Docker image:
    ```sh
    docker pull amanovishnu/cold-connect:latest
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8501:8501 amanovishnu/cold-connect:latest
    ```

3. Open **`http://localhost:8501`** in your browser to use the Streamlit application.

### File Structure

```sh
├── .github                   <- GitHub configuration directory (e.g., workflows for CI/CD)
├── notebook                  <- Directory containing Jupyter notebook and portfolio CSV file
│   └── my_portfolio.csv      <- Sample portfolio CSV file
├── .dockerignore             <- Specifies files and directories to ignore when building the Docker image
├── .env                      <- Environment variables file (not included in the repository)
├── .gitignore                <- Git ignore file
├── app.py                    <- Main Streamlit application file
├── chains.py                 <- Contains the Chain class for extracting jobs and generating messages
├── Dockerfile                <- Dockerfile for containerizing the application
├── LICENSE                   <- License file
├── portfolio.py              <- Contains the Portfolio class for managing and querying portfolio links
├── README.md                 <- Project README file
├── requirements.txt          <- List of Python dependencies
├── setup.cfg                 <- Configuration for flake8 and mypy
└── utils.py                  <- Utility functions for cleaning text and fetching model lists

```


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