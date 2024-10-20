#!/usr/bin/python3

""" Prime Game, determine the winner of the game """


def is_prime(n):
    """ check if a number is prime """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(n):
    """ count the number of prime numbers in a given range """
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count


def isWinner(x, nums):
    """ a function to determine the winner of the game """

    bob = 0
    maria = 0

    for n in nums:
        prime_count = count_primes(n)
        if prime_count % 2 == 0:
            bob += 1
        else:
            maria += 1

    if bob > maria:
        return "Bob"
    if bob < maria:
        return "Maria"
    return None
