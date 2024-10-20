#!/usr/bin/python3

""" Prime Game, determine the winner of the game """


def sieve_of_eratosthenes(n):
    """ Returns a list where index i is True if i is prime, False otherwise """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def prime_count_up_to_n(sieve, n):
    """ Returns the number of primes up to n using the sieve """
    return sum(sieve[:n + 1])


def isWinner(x, nums):
    """ Determines the winner of the game after x rounds """
    # Determine the maximum number in nums to optimize sieve size
    max_n = max(nums)

    # Create a sieve of primes up to max_n
    sieve = sieve_of_eratosthenes(max_n)

    # Track the number of wins for each player
    maria_wins = 0
    bob_wins = 0

    for n in nums:
        primes_up_to_n = prime_count_up_to_n(sieve, n)

        # If the number of primes is odd, Maria wins (since she goes first)
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            bob_wins += 1

    # Determine the overall winner
    if maria_wins > bob_wins:
        return "Maria"
    elif bob_wins > maria_wins:
        return "Bob"
    else:
        return None
