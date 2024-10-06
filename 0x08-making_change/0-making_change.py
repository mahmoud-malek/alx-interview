#!/usr/bin/python3

""" Making Change """


def makeChange(coins, total):
    """ Given a pile of coins of different values,
    determine the fewest number of coins needed
             to meet a given amount total """
    if total <= 0:
        return 0
    idx = 0
    seen = {}
    min_path = float('inf')

    def db(total):
        # base case
        if total == 0:
            return 0
        if total in seen:
            return seen[total]
        if total < 0:
            return float('inf')

        # recursive case
        min_coins = float('inf')
        for c in coins:
            if c <= total:
                num_coins = db(total - c)
                min_coins = min(min_coins, num_coins + 1)
        seen[total] = min_coins
        return min_coins

    min_path = db(total)
    if min_path == float('inf'):
        return -1
    return min_path
