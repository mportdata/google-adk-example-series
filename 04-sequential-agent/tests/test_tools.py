from daily_forecast.sub_agents.daily_context_getter.tools import (
    geocode_city,
    daily_forecast,
    is_public_holiday,
    good_outdoor,
)
from daily_forecast.sub_agents.country_code_exrtractor.tools import (
    get_country_code_html,
)
from datetime import date, timedelta, datetime


def test_geocode_city() -> int:

    geocode_city_response = geocode_city("Manchester")

    assert geocode_city_response == {
        "lat": 53.48095,
        "lon": -2.23743,
        "name": "Manchester",
    }


def test_daily_forecast():

    location_name = "Manchester"

    three_days_ahead = date.today() + timedelta(days=3)

    daily_forecast_response = daily_forecast(location_name, three_days_ahead)

    print(
        f"{location_name} has a forcase of {daily_forecast_response} on {three_days_ahead}"
    )

    assert type(daily_forecast_response) == dict
    assert type(daily_forecast_response["temp_max"]) == float
    assert type(daily_forecast_response["temp_min"]) == float
    assert type(daily_forecast_response["precip_prob"]) == int
    assert daily_forecast_response["precip_prob"] >= 0


def test_is_public_holiday_true():
    country_code = "GB"
    christmas_day = "2025-12-25"
    is_public_holiday_response = is_public_holiday(country_code, christmas_day)
    assert is_public_holiday_response["is_holiday"] == True


def test_is_public_holiday_false():
    country_code = "GB"
    christmas_day = "2025-12-24"
    is_public_holiday_response = is_public_holiday(country_code, christmas_day)
    assert is_public_holiday_response["is_holiday"] == False


def test_good_outdoor():
    location_name = "Manchester"
    three_days_ahead = date.today() + timedelta(days=3)
    three_days_ahead_string = str(three_days_ahead)
    good_outdoor_response = good_outdoor(location_name, three_days_ahead_string)
    assert type(good_outdoor_response) == bool


def test_get_country_code_html():
    country_code_html = get_country_code_html()

    assert country_code_html[:15] == "<!DOCTYPE html>"
    assert country_code_html[-8:] == "</html>\n"
