import requests


def get_current_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raise HTTPError if status != 200
        data = response.json()

        try:
            bitcoin_price = data["bitcoin"]["usd"]
            return bitcoin_price
        except (KeyError, TypeError) as e:
            print(f"Error parsing JSON response: {e}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None
