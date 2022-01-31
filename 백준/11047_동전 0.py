import sys
n,k = map(int,sys.stdin.readline().rstrip().split())
money = []
for _ in range(n):
    money.append(int(sys.stdin.readline().rstrip()))
money.sort(reverse=True)
result = 0
for bills in money:
    result += k//bills
    k %= bills
print(result)
