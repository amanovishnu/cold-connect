import os

from dotenv import load_dotenv
from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()


class Chain:
    def __init__(self, api_key, temperature=0.1, model_name="llama-3.3-70b-versatile"):
        self.api_key = api_key
        self.llm = ChatGroq(temperature=temperature, groq_api_key=api_key, model_name=model_name)

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: 
            `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links, username="john_dawson", referrer_name="jane_potter", message_type="e-mail"):
        if message_type == "e-mail":
            prompt = PromptTemplate.from_template(
                """
                ### JOB DESCRIPTION:
                {job_description}
                ### INSTRUCTION:
                You are {username}, an aspiring full-stack engineer with over 5 years of professional experience
                in developing and deploying web applications using modern technologies.
                You are actively seeking job opportunities and looking for potential candidates who can provide referrals.
                you found out that {referrer_name} is working at the company that posted the job.
                Your task is to craft a cold {message_type} to a potential referrer, requesting them to refer you for the job.
                highlighting your skills and expertise in meeting their organization's needs.
                Include the most relevant links from the provided portfolio: {link_list}.
                Remember, you are {username}, an aspiring full-stack engineer.
                and you are looking for a referral from {referrer_name}.
                Do not include any preamble.
                Make sure the {message_type} is professional and concise.
                ### EMAIL (NO PREAMBLE):
                ### DON'T USE WORKS LIKE "dear", "sweetheart" INSTEAD USE "Hello", "Hi"
                """
            )
        else:
            prompt = PromptTemplate.from_template(
                """
                ### JOB DESCRIPTION:
                {job_description}
                ### INSTRUCTION:
                You are {username}, an aspiring full-stack engineer with over 5 years of professional experience
                in developing and deploying web applications using modern technologies.
                You are actively seeking job opportunities and looking for potential candidates who can provide referrals.
                you found out that {referrer_name} is working at the company that posted the job and you are reaching him/her out on linkedin.
                Asking him/her to refer you for the job.
                Your task is to craft a message to {referrer_name}, requesting him/her to refer you for the job.
                highlighting your skills and expertise in meeting their organization's needs.
                Include the most relevant links from the provided portfolio: {link_list}.
                Remember, you are {username}, an aspiring full-stack engineer.
                and you are looking for a referral from {referrer_name}.
                Do not include any preamble.
                Make sure the {message_type} is professional and concise and strictly under 1000 characters.
                ### MESSAGE (NO PREAMBLE):
                ### DON'T USE WORKS LIKE "dear", "sweetheart" INSTEAD USE "Hello", "Hi"
                ### MAKE SURE THE CONTENT IS CONCISE AND UNDER 1000 CHARACTERS
                ### STRICTLY FOLLOW THE INSTRUCTION REMEMBER YOU ARE ASKING FOR A REFERRAL FROM {referrer_name}
                """
            )
        chain_email = prompt | self.llm
        res = chain_email.invoke({
            "job_description": str(job),
            "link_list": links,
            "username": username,
            "referrer_name": referrer_name,
            "message_type": message_type
        })
        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
