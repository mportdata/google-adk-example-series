from bitcoin_bard.tools import get_current_bitcoin_price


def test_get_current_bitcoin_price() -> int:
    """Retrieves the current price of Bitcoin in USD.

    Returns:
        int: The current price of Bitcoin prices in USD as an integer.
    """
    current_bitcoin_price = get_current_bitcoin_price()

    assert (
        current_bitcoin_price >= 0
    ), "Returned Bitcoin price not greater than or equal to 0."
    assert (
        type(current_bitcoin_price) == int
    ), "Returned Bitcoin price not of type integer as expected."
