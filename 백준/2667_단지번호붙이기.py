import sys 
from collections import deque

read = sys.stdin.readline 
N = int(read())
graph = []
for _ in range(N):
    graph.append(list(map(int,list(read().rstrip()))))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False for _ in range(N)] for _ in range(N)]

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True 
    cnt = 1
    while queue:
        x, y = queue.popleft()  
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True 
                cnt += 1
    return cnt

num_danji = 0
results = []
for i in range(N):
    for j in range(N):
        # graph[i][j] == 1 이고, 방문하지 않은 곳에서만 BFS 호출
        if graph[i][j] == 1 and not visited[i][j]:
            num_danji += 1
            results.append(bfs(i, j))

print(num_danji)  # 단지 수 출력
for result in sorted(results):  # 각 단지 크기 오름차순 출력
    print(result)
