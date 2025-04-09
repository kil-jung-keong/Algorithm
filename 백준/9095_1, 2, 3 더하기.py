import sys
T = int(sys.stdin.readline().rstrip())
n = []
for _ in range(T):
    n.append(int(sys.stdin.readline().rstrip()))
def dp(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 4
    else:
        return dp[a-1] + dp[a-2] + dp[a-3]


for i in range(len(n)):
    print(dp(n[i]))