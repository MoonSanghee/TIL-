n, k = map(int, input().split())
dp = [0 for _ in range(k + 1)]
items = []
for i in range(n):
    items.append(list(map(int,input().split())))
for item in items:
    w, v = item
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)
print(dp[-1])