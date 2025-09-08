import requests


def get_current_bitcoin_price() -> dict:
    """
    Fetches the current Bitcoin price in USD using the CoinGecko API.

    The function makes a GET request to CoinGecko's `/simple/price` endpoint.
    If the request is successful and the response is valid JSON, the current
    Bitcoin price in USD is extracted and returned.

    Returns
    -------
    dict
        A dictionary with a single key 'current_bitcoin_price':
        - On success: the Bitcoin price as a float or int.
        - On JSON parse error: an error message string.
        - On request failure: an error message string.
    """
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raise HTTPError if status != 200
        data = response.json()

        try:
            bitcoin_price = data["bitcoin"]["usd"]
            return {"current_bitcoin_price": bitcoin_price}
        except (KeyError, TypeError) as e:
            return {"current_bitcoin_price": f"Error parsing JSON response: {e}"}

    except requests.exceptions.RequestException as e:
        return {"current_bitcoin_price": f"Error fetching Bitcoin price: {e}"}
