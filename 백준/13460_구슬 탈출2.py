import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
data = []
for _ in range(m):
    data.append(list(sys.stdin.readline().rstrip()))
print(data)
