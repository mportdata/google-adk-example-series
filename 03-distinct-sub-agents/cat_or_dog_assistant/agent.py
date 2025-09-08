from google.adk.agents import Agent
from .sub_agents import cat_assistant_agent, dog_assistant_agent

root_agent = Agent(
    name="cat_or_dog_assistant",
    model="gemini-2.0-flash",
    description="The first agent someone speaks to before being redirected to the cat assitant or the dog assistant.",
    instruction=(
        """
            Greet the user explaining you are here to provide assistance with either their cat or their dog.
            Determine whether a user is asking for assistance with a cat or a dog and then redirect them to the appropriate agent.
            You have access to the following sub agents:
                - cat_assistant_agent
                - dog_assistant_agent
            Please reiterate you can only provide assistance for a cat or a dog if it is not clear which of the two pets they need assistance with.
        """
    ),
    sub_agents=[cat_assistant_agent, dog_assistant_agent],
)
