import sys 
from collections import deque
from unittest import result

read = sys.stdin.readline 
R, C, T = map(int,read().split())
graph = []
for _ in range(R):
    graph.append(list(map(int, read().split())))

# 공기청정기 위치 구하고 초기화 하기
air_fresh = []
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            air_fresh.append((i,j))
            graph[i][j] = 0
air_fresh.sort()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 미세먼지 확산
''' 키포인트 : graph[i][j] -= (graph[i][j] // 5) 해버리면
grpah의 값이 계속 변화하기 때문에 정상적인 업데이트가 불가능하다. 
'''
def spread():
    new_graph = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0:
                spread_count = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < R and 0 <= nj < C and (ni,nj) != air_fresh[0] and (ni,nj) != air_fresh[1]:
                        new_graph[ni][nj] += (graph[i][j] // 5)
                        spread_count += 1
                new_graph[i][j] += graph[i][j] - (graph[i][j] // 5) * spread_count
    return new_graph

def air_fresher():
    up_line = []
    down_line = []
    up_x, up_y = air_fresh[0]
    down_x, down_y = air_fresh[1]
    # 우 상 좌 하
    while 0 <= up_y < C - 1:
        up_y += 1
        up_line.append((up_x,up_y))
    while 0 < up_x < R:
        up_x -= 1
        up_line.append((up_x,up_y))
    while 0 < up_y < C:
        up_y -= 1
        up_line.append((up_x,up_y))
    while 0 <= up_x < air_fresh[0][0] - 1:
        up_x += 1
        up_line.append((up_x,up_y))
    
    # 우 하 좌 상
    while 0 <= down_y < C - 1:
        down_y += 1
        down_line.append((down_x,down_y))    
    while 0 <= down_x < R - 1:
        down_x += 1
        down_line.append((down_x,down_y))    
    while 0 < down_y < C:
        down_y -= 1
        down_line.append((down_x,down_y))  
    while down_x > air_fresh[1][0]:
        down_x -= 1
        down_line.append((down_x,down_y))   
    return up_line, down_line 

for _ in range(T):
    result_graph = [[0 for _ in range(C)] for _ in range(R)]
    spread_graph = spread()
    up_line, down_line = air_fresher()
    for i in range(len(up_line)-1):
        x,y = up_line[i][0], up_line[i][1]
        nx,ny = up_line[i+1][0], up_line[i+1][1]
        result_graph[nx][ny] = spread_graph[x][y]
    for i in range(len(down_line)-1):
        x,y = down_line[i][0], down_line[i][1]
        nx,ny = down_line[i+1][0], down_line[i+1][1]
        result_graph[nx][ny] = spread_graph[x][y]
    result_graph[air_fresh[0][0]][air_fresh[0][1]] = 0
    result_graph[air_fresh[1][0]][air_fresh[1][1]] = 0
    for i in range(R):
        for j in range(C):
            if (i,j) not in up_line and (i,j) not in down_line:
                result_graph[i][j] = spread_graph[i][j]
    graph = result_graph
    
cnt = sum(sum(row) for row in graph)
print(cnt)
