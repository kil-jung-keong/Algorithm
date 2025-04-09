from platform import java_ver
import sys 
from collections import deque 

read = sys.stdin.readline
N, L, R = map(int, read().split())
population = []

for _ in range(N):
    population.append(list(map(int,read().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs로 각 칸을 탐색하여 L~R사이인지 판단한다. 
def bfs(r,c):
    q = deque()
    q.append((r,c))
    visited[r][c] = True 
    union = []
    union.append((r,c))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < N and ny < N and nx >= 0 and ny >= 0 and not visited[nx][ny]:
                if L <= abs(population[nx][ny] - population[x][y]) <= R:
                    visited[nx][ny] = True 
                    q.append((nx,ny))
                    union.append((nx,ny))
    return union 

all_unions = []
cnt = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    is_union = False
    for i in range(N):
        for j in range(N):
            union = bfs(i,j) # 한번의 탐색에서 직접 연결된 좌표들만 탐색하므로, 다른 좌표에서 형성될 수 있는 연합을 탐색하지 못함
            if len(union) > 1:
                all_unions.append(union)
                is_union = True 
    
    # 한번의 이동에서 모든 연합을 모은 다음 인구를 재분배한다. 
    if not is_union:
        break 
    for union in all_unions:
        total_population = sum(population[x][y] for x,y in union)
        avg = total_population // len(union)
        for x,y in union:
            population[x][y] = avg 
    cnt += 1

print(cnt)
