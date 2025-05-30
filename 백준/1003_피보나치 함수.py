import sys 

read = sys.stdin.readline 

T = int(read())

# N의 최대 입력값이 40 이므로 미리 설정
dp = [(0,0)] * 41 
dp[0] = (1,0)
dp[1] = (0,1)

for i in range(2, 41):
    dp0 = dp[i - 1][0] + dp[i - 2][0]
    dp1 = dp[i - 1][1] + dp[i - 2][1]
    dp[i] = (dp0, dp1)

for _ in range(T):
    N = int(read())
    print(dp[N][0], dp[N][1])
