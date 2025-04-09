import sys 
from collections import deque

read = sys.stdin.readline 
N, M = map(int, read().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,(list(read().rstrip())))))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False for _ in range(M)] for _ in range(N)]
def bfs(x,y):
    queue = deque([(x,y,1)])
    visited[x][y] = True 
    while queue:
        x,y,cnt = queue.popleft()
        if x == N - 1 and y == M - 1:
            return cnt 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True 
                queue.append((nx,ny,cnt+1))
    return -1

print(bfs(0,0))

