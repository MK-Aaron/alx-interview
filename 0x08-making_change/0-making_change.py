#!/usr/bin/python3

def makeChange(coins: list, total: int) -> int:
    """
    Finds the optimal number of coins can sum up to a total
    coins: is a list of coins that I can use to check the total
    total: the sumbeing subtracted from
    Return: an interger
    """

    if total <= 0:
        return 0

    coins.sort()

    # dynamic programming list
    dp = [float('inf')] * (total + 1)

    dp[0] = 0  # Base case

    for coin in coins:
        for amt in range(coin, total + 1):
            dp[amt] = min(dp[amt], dp[amt - coin] + 1)

    if dp[total] != float('inf'):
        return dp[total]
    else:
        return -1
