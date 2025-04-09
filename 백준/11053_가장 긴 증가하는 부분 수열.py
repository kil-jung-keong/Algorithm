import sys 

read = sys.stdin.readline 
N = int(read())
numbers = list(map(int, read().split()))

# dp[i] = i번째 원소를 마지막 원소로 하는 가장 긴 부분수열의 길이
# dp 테이블 초기화 
dp = [1] * N 

for i in range(1,N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
