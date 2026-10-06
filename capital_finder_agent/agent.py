from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel, Field


class CapitalOutput(BaseModel):
    capital: str  = Field(description="The capital of country")




root_agent = Agent(
    model='gemini-3.5-flash',
    name='capital_finder',
    description='Returns country capital information in a structured schema.',
    instruction=""" You are a capital information agent. Given a country
    , respond ONLY with a JSON object containing the capital.
    Format: {"capital": "capital_name"}
    """,
    output_schema=CapitalOutput
    output_key="found_capital"      # Store  agent response in session.state["found_capital"]
)
