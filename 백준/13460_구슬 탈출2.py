# Queue에 빨간 구슬의 (X, Y) 좌표, 파란 구슬의 (X, Y) 좌표를 모두 넣는다.
# 방문 여부를 확인할 check 배열을 4차원 배열로 선언한다. 배열의 인덱스는 [빨간 X좌표] [빨간 Y좌표] [파란 X좌표] [파란 Y좌표] 이다.
# 구슬을 굴릴 때, 구슬의 다음 위치가 벽(#)인지, 구슬의 현재 위치가 구멍(O)인지 확인한다.
# 구슬의 다음 위치가 벽이라면 앞으로 가지 못한다. 구슬의 현재 위치가 구멍이라면, 현재 구슬의 색이 무엇인지 판별한다.
# 만약 파란 구슬의 현재 위치가 구멍이라면 무시하고, 빨간 구슬의 현재 위치가 구멍이라면, 1을 출력하고 종료한다.
# 구슬을 굴리면서, 빨간 구슬의 이동 거리와 파란 구슬의 이동 거리를 카운트해야 한다.
# 구슬을 굴린 후, 빨간 구슬의 위치와 파란 구슬의 위치가 같다면, 이동 거리 비교를 통해 겹치지 않도록 처리해야 한다.
# 만약 구슬이 겹쳤다면, 굴릴 때 카운트했던 이동 거리가 더 긴 구슬의 위치를 한 칸 이전으로 되돌린다.
# 굴리는 과정이 10번을 넘어가면 그대로 종료하고, 0을 출력한다.
# 더 이상 갈 곳이 없을 때에는 BFS를 빠져나와서 0을 출력한다.


import sys
from collections import deque
# 입력
n, m = map(int, sys.stdin.readline().rstrip().split())
data = [list(input().rstrip()) for _ in range(n)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# queue
queue = []

# 방문 맵
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

# R,B,O 위치
def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'R':
                rx = i
                ry = j
            elif data[i][j] == 'B':
                bx = i
                by = j
    queue.append((rx,ry,bx,by,1))
    visited[rx][ry][bx][by] = True

# 이동
def move(x,y,dx,dy):
    cnt = 0
    # 다음이 벽이거나 지금이 구멍일 때까지
    while data[x+dx][y+dy] != '#' and data[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

# 조건 문
def solve():
    init()
    while queue:
        rx, ry, bx, by, depth = queue.pop(0)
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx,ry,dx[i],dy[i])
            nbx, nby, bcnt = move(bx,by,dx[i],dy[i])
            if data[nbx][nby] != 'O':
                if data[nrx][nry] == 'O':
                    print(depth)
                    return
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx,nry,nbx,nby,depth+1))
    print(-1)
            
solve()