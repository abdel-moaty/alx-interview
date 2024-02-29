#!/usr/bin/python3

"""
Determine fewest number of coins needed to meet given amount total.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total.

    Args:
        coins (List[int]): List of coin denominations.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
            Returns -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_used = 0
    for coin in coins:
        coin_used += total // coin
        total %= coin
        if total == 0:
            return coin_used
    return -1
