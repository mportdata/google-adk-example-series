from google.adk.agents import Agent
from .tools import empty_litter_tray, order_catnip

root_agent = Agent(
    name="cat_assistant_agent",
    model="gemini-2.0-flash",
    description="The cat assistant agent can help with tasks required to do for your cat.",
    instruction=(
        """
            You are a cat assitant. You are able to help an owner with tasks related to cat ownsership.
            You have access to the following tools:
                - empty_litter_tray
                - order_catnip # this requires the amount of catnip to order in grams
        """
    ),
    tools=[empty_litter_tray, order_catnip],
)
