import os
import sys

# un-comment it to run job_search file seperately
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.models.job_search_model import ExtractSchema


from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Initialize the agent with DuckDuckGo tool
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a job search assistant that provides job listings based on user skills and experience.",
    tools=[DuckDuckGoTools()],
    markdown=True
)

# Define the user query
user_query = {
    "skills": "Python",
    "location": "Banglore",
    "job_profile": "Data Scientist",
    "years_of_experience": 3
}

# Construct the search query
search_query = f"{user_query['job_profile']} jobs in {user_query['location']} requiring {user_query['skills']} with {user_query['years_of_experience']} years of experience"

# Generate the agent's response
# response = agent.print_response(f"Search for: {search_query}")
# print(response)

structured_output_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a job search assistant that provides job listings based on user skills and experience.",
    instructions="You must accurately provide job link of the website where you find the jobs",
    response_model=ExtractSchema,
    markdown=False
)

structured_output_agent.print_response(f"Search for: {search_query}")

# data = structured_output_agent.run("Search for: {search_query}")
# print(data)