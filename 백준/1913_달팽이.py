import sys 

read = sys.stdin.readline 
N = int(read())
M = int(read())

arr = [[0 for _ in range(N)] for _ in range(N)]

# 하우상좌
dx = [1,0,-1,0]
dy = [0,1,0,-1]

dir = 0
num = N ** 2
x, y = 0, 0
while num > 0:
    arr[x][y] = num 
    if num == M:
        target_x, target_y = x + 1, y + 1
    
    nx, ny = x + dx[dir], y + dy[dir]

    if not (0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0):
        dir = (dir+1) % 4
        nx, ny = x + dx[dir], y + dy[dir]
    
    x, y = nx, ny 
    num -= 1

for row in arr:
    print(*row)

print(target_x, target_y)





