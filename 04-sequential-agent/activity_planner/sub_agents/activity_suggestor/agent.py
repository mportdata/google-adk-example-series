from google.adk.agents import Agent
from .tools import is_public_holiday, good_outdoor, parse_date
from .types import DailyContextOutput

root_agent = Agent(
    name="activity_suggestor",
    model="gemini-2.0-flash",
    description="This agent determines whether or not the weather is suitbale for outdoor activities, if it is a public holiday on the given day and then uses that to suggest 5 fun acitvities to do on that day.",
    instruction=(
        """
            Your job is to return whether or not the weather is forecast to be a good and whether or not it is a public holiday for a given location on a given day.
            IMPORTANT: Before passing date strings to tools ensure they are of the form YYYY-MM-DD.
            Whether or not it is a public holiday can be found by providing the two character public code and the date to the following tool:
                - is_public_holiday(country_code: str, date: str)
            Wheter or not the weater is forecast to be good can be found by providing the full location name and the given date to the following tool:
                - good_outdoor(name: str, date: str)
            IMPORTANT: You must have received a country name, country code and date before proceeding.
            OUTPUT: Given the status of the outdoor weather and if it is a public holiday and the location suggest 5 fun activities to do on that day.
        """
    ),
    tools=[is_public_holiday, good_outdoor],
)
