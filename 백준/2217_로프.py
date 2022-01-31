import sys
n = int(sys.stdin.readline().rstrip())
weight = []
for _ in range(n):
    weight.append(int(sys.stdin.readline().rstrip()))
weight.sort(reverse=True)
answer = 0
for i in range(n):
    weight[i] = weight[i] * (i+1)
print(max(weight))    