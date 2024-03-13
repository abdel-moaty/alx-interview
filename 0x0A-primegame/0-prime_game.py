#!/usr/bin/python3

"""Prime Game"""


def isWinner(x, nums):
    """Returns name of the player that won the most rounds."""
    if x < 1:
        return None
    maria_score, ben_score = 0, 0
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i*i, max_num + 1, i):
                primes[j] = False
    for n in nums:
        primes_count = sum(1 for i in range(2, n + 1) if primes[i])
        ben_score += primes_count % 2 == 0
        maria_score += primes_count % 2 == 1
    if maria_score == ben_score:
        return None
    return 'Maria' if maria_score > ben_score else 'Ben'
