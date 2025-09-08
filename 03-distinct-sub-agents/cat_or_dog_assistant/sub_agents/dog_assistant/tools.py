from datetime import datetime as dt


def take_for_walk(distance_km: float) -> dict:
    """
    Simulates taking a dog for a walk.

    Returns
    -------
    dict
        A dictionary with a single key 'action_taken' describing how long of a walk the dog was taken on and when it happened.
    """
    response = {"action_taken": f"The dog was walked for {distance_km}km at {dt.now()}"}
    return response


def refill_water_bowl() -> dict:
    """
    Simulates refilling a dogs water bowl.

    Returns
    -------
    dict
        A dictionary with a single key 'action_taken' describing when the dog's water bown was refilled.
    """
    response = {"action_taken": f"Dogs water bowl refilled at {dt.now()}"}
    return response
