import sys
from collections import deque 

# 입력 
read = sys.stdin.readline 
N = int(read())
graph = []
for _ in range(N):
    graph.append(list(map(int, read().split())))

# 아기상어 위치 
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            start_x = i
            start_y = j
            graph[i][j] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,size):
    queue = deque([(x,y,0)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True 
    fishes = []
    while queue:
        x,y,dist = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if size >= graph[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny,dist+1))
                    if 0 < graph[nx][ny] < size:
                        fishes.append((dist+1,nx,ny))
    if fishes:
        fishes.sort()
        return fishes[0]
    return None  

fish_size = 2
fish_cnt = 0
time = 0
while True:
    if bfs(start_x, start_y, fish_size) is None:
        break 
    dist, x, y = bfs(start_x, start_y, fish_size)
    fish_cnt += 1
    time += dist
    if fish_cnt == fish_size:
        fish_size += 1
        fish_cnt = 0
    start_x = x
    start_y = y
    graph[start_x][start_y] = 0

print(time)