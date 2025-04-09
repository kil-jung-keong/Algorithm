import sys 
from collections import deque

read = sys.stdin.readline 

N, M = map(int, read().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, read().split())))

# 상하좌우 
dx = [-1,1,0,0]
dy = [0,0,-1,1]      

# 경계 검사 함수
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M

# 다 녹았는지 검사
def is_melt(graph):
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                return False 
    return True 

# 1년 후 빙산 상태 
def after_one_year(graph):
    new_graph = [row[:] for row in graph]  # 기존 그래프 복사
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:  # 현재 위치가 0이 아닐 때만
                cnt = sum(1 for k in range(4) if is_valid(i + dx[k], j + dy[k]) and graph[i + dx[k]][j + dy[k]] == 0)
                new_graph[i][j] -= cnt
                if new_graph[i][j] < 0:
                    new_graph[i][j] = 0
    return new_graph

def bfs(x,y,visited,graph):
    queue = deque([(x,y)])
    visited[x][y] = True 
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True 
                queue.append((nx,ny))

def result(graph):
    year_cnt = 0
    while True:
        # 녹기 전 빙산 덩어리 수 확인
        visited = [[False for _ in range(M)] for _ in range(N)]
        ice_cnt = 0

        for i in range(N):
            for j in range(M):
                if graph[i][j] != 0 and not visited[i][j]:
                    ice_cnt += 1
                    bfs(i, j, visited, graph)

        if ice_cnt >= 2:  # 빙산이 분리된 경우
            return year_cnt
        if is_melt(graph):  # 모든 빙산이 녹은 경우
            return 0

        # 1년 경과
        graph = after_one_year(graph)
        year_cnt += 1

print(result(graph))