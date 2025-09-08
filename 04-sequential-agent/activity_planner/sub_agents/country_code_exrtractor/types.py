from pydantic import BaseModel, Field


class CountryCodeOutput(BaseModel):
    country_name: str = Field(description="The full country name.")
    country_code: str = Field(
        description="The corresponding country code.", pattern=r"^[A-Z]{2}$"
    )
    context_date: str = Field(description="The date given by the user.")
