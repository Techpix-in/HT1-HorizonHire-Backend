from typing import List
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from firecrawl import FirecrawlApp
from src.models.job_search_model import ExtractSchema
from dotenv import load_dotenv

# un-comment it to run job_search file seperately
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# from src.models.job_search_model import ExtractSchema

# load_dotenv()

# firecrawl_api_key = os.getenv("FIRE_CRAWL_API_KEY")
# openai_api_key = os.getenv("OPENAI_API_KEY")
# model_id  = os.getenv("MODEL")

class JobHuntingAgent:
    
    def __init__(self, firecrawl_api_key: str, openai_api_key: str, model_id: str):
        # self.agent = Agent(
        #     model=OpenAIChat(id=model_id, api_key=openai_api_key),
        #     markdown=True,
        #     description="You are a career expert who helps find job opportunities based on user preferences."
        # )
        self.firecrawl = FirecrawlApp(api_key=firecrawl_api_key)
        # self.redis_client = Redis()

    def find_jobs(
        self, 
        job_title: str,
        location: str,
        experience_years: int,
        skills: List[str]
    ) -> str:
        # formatting keys
        formatted_job_title = job_title.lower().replace(" ", "-")
        formatted_location = location.lower().replace(" ", "-")
        skills_string = ", ".join(skills)
        urls = [
            f"https://www.naukri.com/{formatted_job_title}-jobs-in-{formatted_location}",
            f"https://www.indeed.com/jobs?q={formatted_job_title}&l={formatted_location}",
            f"https://www.monster.com/jobs/search/?q={formatted_job_title}&where={formatted_location}",
        ]
        
        print(f"Searching for jobs with URLs: {urls}")
        
        try:
            raw_response = self.firecrawl.extract(
                urls=urls,
                params={
                    'prompt': f"""Extract job postings by region, roles, job titles, and experience from these job sites.
                    
                    Look for jobs that match these criteria:
                    - Job Title: Should be related to {job_title}
                    - Location: {location} (include remote jobs if available)
                    - Experience: Around {experience_years} years (optional)
                    - Skills: Should match at least some of these skills: {skills_string}
                    - Job Type: Full-time, Part-time, Contract, Temporary, Internship (optional)
                    
                    For each job posting, extract:
                    - region: The broader region or area where the job is located (e.g., "Northeast", "West Coast", "Midwest")
                    - role: The specific role or function (e.g., "Frontend Developer", "Data Analyst")
                    - job_title: The exact title of the job
                    - experience: The experience requirement in years or level (e.g., "3-5 years", "Senior")
                    - job_link: The link to the job posting
                    
                    IMPORTANT: You **MUST** Return data for at least 5 different job opportunities even if **criteria is not fully full-filled**. MAXIMUM 10.
                    """,
                    'schema': ExtractSchema.model_json_schema()
                }
            )
            
            print("Raw Job Response:", raw_response)
            jobs = []
            if isinstance(raw_response, dict) and raw_response.get('success'):
                jobs = raw_response['data'].get('job_postings', [])
            
            if jobs:
                print("Processed Jobs:", jobs)
                return jobs
            else:
                return None
            
            
        except Exception as e:
            print(f"Error in find_jobs: {str(e)}")
            return f"An error occurred while searching for jobs: {str(e)}\n\nPlease try again with different search parameters or check if the job sites are supported by Firecrawl."


# if __name__ == "__main__":

#     job_hunting_agent = JobHuntingAgent(firecrawl_api_key=firecrawl_api_key,openai_api_key=openai_api_key,model_id=model_id)
#     response = job_hunting_agent.find_jobs(job_title="software development",location="bangalore",experience_years=3,skills=["python"])
#     print(response)
#     pass