import sys 

read = sys.stdin.readline 
string1 = read().rstrip()
string2 = read().rstrip()

len1, len2 = len(string1), len(string2)

dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

for i in range(1,len1 + 1): # s1 문자열 순회
    for j in range(1, len2 + 1): # s2 문자열 순회  
        if string1[i - 1] == string2[j - 1]: # 마지막 문자가 같으면
            dp[i][j] = dp[i - 1][j - 1] + 1
        else: # 문자가 다르면 
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len1][len2])

