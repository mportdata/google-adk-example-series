from google.adk.agents import Agent
from .tools import get_country_code_html
from .types import CountryCodeOutput

root_agent = Agent(
    name="country_code_extractor",
    model="gemini-2.0-flash",
    description="This agent finds the country code corresping to a given countries name from a table found in a html text.",
    instruction=(
        """
            Your job is to return the countries name and it's corresponding country code.
            The country code can be found in a html text which you can get from the following tool:
                - get_count_code_html
            IMPORTANT: You must only provide a country code if you can find it in the list. You are allowed to account for misspelt names
            or aliases such as United Kingdom or Great Britain. 
            IMPORTANT: Do not proceed until you have received both a location name and a date from the user. 
            If the name of a city or town infer the country if you can do with confidence, otherwise ask for clarity.
        """
    ),
    output_schema=CountryCodeOutput,
    tools=[get_country_code_html],
)
