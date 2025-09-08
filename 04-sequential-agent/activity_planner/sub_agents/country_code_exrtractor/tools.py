import requests


def get_country_code_html():
    url = "https://date.nager.at/Country"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.text
