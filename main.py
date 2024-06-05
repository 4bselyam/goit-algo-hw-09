def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= count * coin
    return result


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [0] * (amount + 1)
    for i in range(1, amount + 1):
        dp[i] = float("inf")
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    result = {}
    remaining = amount
    for coin in coins:
        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining -= count * coin
    return result


print(find_coins_greedy(49))
print(find_min_coins(49))
