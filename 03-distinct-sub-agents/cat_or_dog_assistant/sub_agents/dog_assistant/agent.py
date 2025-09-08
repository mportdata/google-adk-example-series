from google.adk.agents import Agent
from .tools import take_for_walk, refill_water_bowl

root_agent = Agent(
    name="doga_assistant_agent",
    model="gemini-2.0-flash",
    description="The dog assistant agent can help with tasks required to do for your dog.",
    instruction=(
        """
            You are a dog assitant. You are able to help an owner with tasks related to dog ownsership.
            You have access to the following tools:
                - take_for_walk # this requires the distance in km you would like your dog to be walked.
                - refill_water_bowl
        """
    ),
    tools=[take_for_walk, refill_water_bowl],
)
