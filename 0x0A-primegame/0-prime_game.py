#!/usr/bin/python3
"""
This module defines a set of functions that solve a challenge that involves
determining a game winner based on the strategic removal of prime numbers
and their multiples from a set of consecutive integers
"""


def isWinner(x, nums):
    """
    Function determines winner
    Args:
        x - number of rounds
        nums - an array of n
        n - last and included int in a set from 1
    Returns:
           Name of the player that won the most rounds
           None, if winner cannot be determined
    """
    def sieve_of_eratosthenes(n):
        """
         Function generates prime numbers up to max number in nums
        """
        s = [True] * (n + 1)
        s[0] = s[1] = False
        primes = []
        for i in range(2, n + 1):
            if s[i]:
                primes.append(i)
                for m in range(i * i, n + 1, i):
                    s[m] = False
        return primes

    def game_winner(n, primes):
        """
        Function determines the winner for a single round
        Args:
            n (int): the maximum number in the round
            primes (list): a list of primes less than or equal to n
        Returns:
            str: "Maria" if Maria wins, "Ben" if Ben wins
        """
        if n < 2:
            return None

        is_prime = [False] * (n + 1)
        for prime in primes:
            if prime > n:
                break
            is_prime[prime] = True

        moves = 0
        while n > 1:
            found_prime = False
            for i in range(2, n + 1):
                if is_prime[i]:
                    moves += 1
                    for j in range(i, n + 1, i):
                        is_prime[j] = False
                    found_prime = True
                    break
            if not found_prime:
                break

        # Maria wins if moves is odd, Ben wins if moves is even
        return "Maria" if moves % 2 != 0 else "Ben"

    if not x or x <= 0 or not nums:
        return None

    # Find the maximum n in nums to optimize prime calculation
    max_n = max(nums)
    if max_n < 2:
        return None

    primes = sieve_of_eratosthenes(max_n)

    # Count wins for each player
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = game_winner(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
