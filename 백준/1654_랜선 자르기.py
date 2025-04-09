import sys 

read = sys.stdin.readline 
K, N = map(int, read().split())
lans = []
for _ in range(K):
    lans.append(int(read()))

def binary_search(data):
    start = 1
    end = max(data)
    while start <= end:
        mid = (start + end) // 2
        target = 0
        for d in data:
            target += (d // mid)
        if N > target:
            end = mid - 1
        else:
            start = mid + 1
    return end 



print(binary_search(lans))