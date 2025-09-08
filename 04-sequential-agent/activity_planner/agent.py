from google.adk.agents import SequentialAgent
from .sub_agents import country_code_extractor_agent, activity_suggestor_agent

root_agent = SequentialAgent(
    name="daily_forecast",
    description="First this agent executes the country code extraction agent to get the country code.",
    sub_agents=[country_code_extractor_agent, activity_suggestor_agent],
)
