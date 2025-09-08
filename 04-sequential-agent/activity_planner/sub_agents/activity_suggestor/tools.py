import requests, datetime as dt


def parse_date(date: str) -> dt.date:
    return dt.datetime.strptime(date, "%Y-%m-%d").date()


def geocode_city(name: str) -> dict:
    r = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": name, "count": 1},
        timeout=10,
    )
    r.raise_for_status()
    d = r.json().get("results", [{}])[0]
    return {"lat": d.get("latitude"), "lon": d.get("longitude"), "name": d.get("name")}


def daily_forecast(name: str, date: str):
    date = parse_date(date)
    geocode_results = geocode_city(name)
    lat = geocode_results["lat"]
    lon = geocode_results["lon"]
    r = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "daily": "precipitation_probability_mean,temperature_2m_max,temperature_2m_min",
            "timezone": "auto",
            "start_date": str(date),
            "end_date": str(date),
        },
        timeout=10,
    )
    r.raise_for_status()
    d = r.json()["daily"]
    return {
        "temp_max": d["temperature_2m_max"][0],
        "temp_min": d["temperature_2m_min"][0],
        "precip_prob": d["precipitation_probability_mean"][0],
    }


def is_public_holiday(country_code: str, date: str):
    year = parse_date(date).year
    r = requests.get(
        f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}", timeout=10
    )
    r.raise_for_status()
    holidays = {h["date"] for h in r.json()}
    return {"is_holiday": date in holidays}


def good_outdoor(name: str, date: str):
    weather = daily_forecast(name, date)
    return weather["precip_prob"] <= 30 and 12 <= weather["temp_max"] <= 28
