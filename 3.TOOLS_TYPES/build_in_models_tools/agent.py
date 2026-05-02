from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.tools import url_context 

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='you are an expert in answering user questions. you can use this following tools to help you answer questions: google_search, url_context',
    tools = [google_search, url_context]
)

