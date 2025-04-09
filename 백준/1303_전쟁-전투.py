import sys
from collections import deque
sys.stdin = open("input.txt")
input=sys.stdin.readline

n,m = map(int,input().replace("\n","").split())
board = []
for _ in range(m):
    board.append(list(input().replace("\n","")))
visited = [[False]*n for _ in range(m)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(i,j):
    answer = 0
    queue = deque([(i,j)])
    color = board[i][j]
    while queue:
        x,y = queue.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            answer += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < m and 0 <= ny < n) and board[nx][ny] == color and (not visited[nx][ny]):
                    queue.append((nx,ny))
    return answer
w_result = 0
b_result = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            answer = bfs(i,j)
            if board[i][j] == 'W':
                w_result += answer**2
            else:
                b_result += answer**2
print(w_result,b_result)
