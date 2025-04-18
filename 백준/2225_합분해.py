import sys 

read = sys.stdin.readline 
N, K = map(int, read().split())

dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

for i in range(K + 1):
    dp[i][0] = 1

for i in range(1, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000
print(dp[K][N])                                         