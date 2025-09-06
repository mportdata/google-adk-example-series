import http.client
import json


def get_current_bitcoin_price():
    # Connect to CoinDesk's free Bitcoin price API
    conn = http.client.HTTPSConnection("api.coindesk.com")
    conn.request("GET", "/v1/bpi/currentprice/USD.json")

    response = conn.getresponse()
    data = response.read()

    # Parse JSON
    price_info = json.loads(data.decode("utf-8"))
    btc_price = price_info["bpi"]["USD"]["rate"]

    return btc_price
