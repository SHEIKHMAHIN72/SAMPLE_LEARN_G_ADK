from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from dotenv import load_dotenv
import os 

load_dotenv('.env')
API_KEY = os.getenv('API_KEY')

# Step 2: Connect to Tavily MCP
tavily_mcp = StreamableHTTPServerParams(
    url=f"https://mcp.tavily.com/mcp/?tavilyApiKey={API_KEY}"
)
root_agent = Agent(
    model='gemini-2.5-flash',
    name='RESERCH AGENT',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge, using the following tools : tavily search',
    tools= [tavily_mcp]
    
)
