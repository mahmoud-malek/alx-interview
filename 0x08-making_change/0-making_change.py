#!/usr/bin/python3

""" Making Change """


def makeChange(coins, total):
    """ Given a pile of coins of different values,
    determine the fewest number of coins needed
                     to meet a given amount total """
    if total <= 0:
        return 0

    db = [float('inf')] * (total + 1)
    db[0] = 0
    for t in range(1, total + 1):
        for c in coins:
            if t >= c:
                db[t] = min(db[t], db[t - c] + 1)

    return db[total] if db[total] != float('inf') else -1
