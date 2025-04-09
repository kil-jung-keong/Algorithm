import sys
n = int(sys.stdin.readline().rstrip())
d = [0] * (n+1)
# d 라는 배열의 index는 문제의 입력 n과 대응하고, index
# 의 값은 연산 최솟값(문제의 출력)에 대응하게 된다. 
# d 에 계산된 값을 저장해둔다. 
for i in range(2,n+1):
    # 1 빼기 연산
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
print(d[n])
