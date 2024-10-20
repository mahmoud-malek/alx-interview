#!/usr/bin/python3

""" Prime Game, determine the winner of the game """


def sieve(n):
    """ generate list of all primes up to n """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            # mark all multiples of (i) prime
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def countPrimes(primes, n):
    """ counts the primes """
    return sum(primes[:n + 1])


def isWinner(x, nums):
    """ a function to determine the winner of the game """

    bob = 0
    maria = 0
    maxN = max(nums)

    primes = sieve(maxN)
    for n in nums:
        primes_n = countPrimes(primes, n)
        if primes_n % 2 == 1:
            maria += 1
        else:
            bob += 1

    if maria > bob:
        return "Maria"
    elif bob > maria:
        return "Bob"
    else:
        return None
