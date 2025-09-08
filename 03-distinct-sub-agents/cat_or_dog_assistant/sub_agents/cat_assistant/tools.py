from datetime import datetime as dt


def empty_litter_tray() -> dict:
    """
    Simulates emptying the cat's litter tray.

    Returns
    -------
    dict
        A dictionary with a single key 'action_taken' describing the time
        the litter tray was emptied.
    """
    response = {"action_taken": f"Litter tray has been emptied at {dt.now()}"}
    return response


def order_catnip(quanitity_grams: int) -> dict:
    """
    Simulates ordering catnip for a cat.

    Returns
    -------
    dict
        A dictionary with a single key 'action_taken' describing how much catnip was ordered in grams and when.
    """
    response = {"action_taken": f"{quanitity_grams}g of catnip ordered at {dt.now()}"}
    return response
