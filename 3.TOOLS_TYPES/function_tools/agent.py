from google.adk.agents.llm_agent import Agent
from google.adk.tools import function_tool
from datetime import datetime
import requests
import os

@function_tool
def get_current_time():
    """Returns the current system time now."""
    return str(datetime.datetime.now())

@function_tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers add return the results."""
    return a + b

@function_tool
def calculate_discount(price: float, discount_percent: float) -> float:
    """calculates a discount on a given price."""
    discount = price * (discount_percent / 100)
    return price - discount 

@function_tool
def list_repos() -> str:
    """Returns a list of my github repositories."""

    token = os.getenv('GITHUB_TOKEN')
    headers = {'"Authorization": f"Bearer {token}"'}

    url = "https://api.github.com/user/repos"
    response = requests.get(url, headers=headers)

    repos = [repo["name"] for repo in response.json()]
    return ", ".join(repos)


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge using the following tools: get_current_time, add_numbers, calculate_discount, list_repos.',
    tools=[get_current_time, add_numbers, calculate_discount, list_repos]
)
