import sys 
from bisect import bisect_left, bisect_right

read = sys.stdin.readline 
N, M = map(int, read().split())
coord = list(map(int, read().split()))
lines = []
for _ in range(M):
    lines.append(list(map(int, read().split())))

coord.sort()
for line in lines:
    start, end = line[0], line[1]
    left_idx = bisect_left(coord, start)
    right_idx = bisect_right(coord, end)
    print(right_idx - left_idx)
