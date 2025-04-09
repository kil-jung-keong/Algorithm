import sys 

read = sys.stdin.readline 
N = int(read())
drinks = list(map(int, read().split()))

drinks.sort()
start, end = 0, N - 1
target_sum = sys.maxsize 
best_pair = (0,0)

while start < end:
    current_sum = drinks[start] + drinks[end]
    if abs(current_sum) < target_sum:
        target_sum = abs(current_sum)
        best_pair = (drinks[start], drinks[end])
    if current_sum < 0:
        start += 1
    else:
        end -= 1

print(best_pair[0],best_pair[1])