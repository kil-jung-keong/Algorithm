import sys 
from bisect import bisect_left, bisect_right

read = sys.stdin.readline 
T = int(input())

def binary_search(target,data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid 
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 

for _ in range(T):
    N = int(input())
    note_1 = list(map(int, read().split()))
    M = int(input())
    note_2 = list(map(int, input().split()))
    note_1.sort()
    for num in note_2:
        if binary_search(num, note_1) is not None:
            print(1)
        else:
            print(0)