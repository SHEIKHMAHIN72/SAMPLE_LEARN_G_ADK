from google.adk.agents.llm_agent import LlmAgent
from pydantic import BaseModel, Field
from datetime import date
'''
# ✅ Input schema (what user sends)
class TodoInput(BaseModel):
    topic: str = Field(description="What the todo list is about")
    deadline: date = Field(description="Final deadline in YYYY-MM-DD format")'''

# ✅ Output schema (what agent returns)
class TodoItem(BaseModel):
    task: str = Field(description="Task name")
    due_date: date = Field(description="YYYY-MM-DD format")
    priority: str = Field(description="low/medium/high")

# ✅ Agent
root_agent = LlmAgent(
    name="todo_agent",
    model="gemini-2.5-flash",
    
    instruction='''
    Generate todo items based on the input.
    Follow the output schema strictly.
    
    Rules:
    - task: clear actionable task
    - due_date: must not exceed input deadline
    - priority: low / medium / high
    ''',

        
    output_schema=TodoItem,     # 👈 OUTPUT schema
    output_key="todo"
)