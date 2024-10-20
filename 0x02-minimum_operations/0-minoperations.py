#!/usr/bin/python3
"""
Minimum Operations module
"""


def minOperations(n):
    if n == 1:
        return 0

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = i
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    return dp[n]
