def rod_cutting(n, prices):
    dp = [0] * (n + 1)
    cuts = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        max_value = 0
        for j in range(1, i + 1):
            if prices[j - 1] + dp[i - j] > max_value:
                max_value = prices[j - 1] + dp[i - j]
                cuts[i] = cuts[i - j] + [j]
        dp[i] = max_value

    return dp[n], cuts[n]

#Let's try
n = 8
prices = [1, 5, 8, 9, 10, 17, 17, 20]
max_profit, cut_lengths = rod_cutting(n, prices)

print(f"Maximum obtainable value: {max_profit}")
print(f"Recommended lengths to cut: {cut_lengths}")
