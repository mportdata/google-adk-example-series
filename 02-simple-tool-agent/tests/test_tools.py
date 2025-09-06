from bitcoin_bard.tools import get_current_bitcoin_price


def test_get_current_bitcoin_price():
    current_bitcoin_price = get_current_bitcoin_price()
    print(current_bitcoin_price)
    return True
