import sys
n = int(sys.stdin.readline().rstrip())
sys.setrecursionlimit(60000)
dp = [0] * (60001)

def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = (fibo(n-1) + fibo(n-2)) % 1000000007

    return dp[n]
print(fibo(n))