from __future__ import annotations

from typing import Dict, List

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int, coins: List[int] | None = None) -> Dict[int, int]:
    coins = sorted(coins or COINS, reverse=True)
    change: Dict[int, int] = {}
    remaining = amount

    for coin in coins:
        if remaining == 0:
            break
        count, remaining = divmod(remaining, coin)
        if count:
            change[coin] = count

    return change


def find_min_coins(amount: int, coins: List[int] | None = None) -> Dict[int, int]:
    coins = sorted(coins or COINS)
    dp = [float("inf")] * (amount + 1)
    prev = [-1] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for current in range(coin, amount + 1):
            if dp[current - coin] + 1 < dp[current]:
                dp[current] = dp[current - coin] + 1
                prev[current] = coin

    if dp[amount] == float("inf"):
        raise ValueError("Суму неможливо скласти з заданих монет")

    change: Dict[int, int] = {}
    remaining = amount
    while remaining > 0:
        coin = prev[remaining]
        change[coin] = change.get(coin, 0) + 1
        remaining -= coin

    return change


def describe_change(change: Dict[int, int]) -> str:
    parts = [f"{coin}×{count}" for coin, count in sorted(change.items(), reverse=True)]
    return ", ".join(parts)


if __name__ == "__main__":
    target = 113
    greedy = find_coins_greedy(target)
    dp = find_min_coins(target)
    print(f"Жадібний алгоритм ({target}): {describe_change(greedy)}")
    print(f"Динамічне програмування ({target}): {describe_change(dp)}")
