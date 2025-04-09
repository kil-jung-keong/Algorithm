import sys 
from collections import deque 

read = sys.stdin.readline 
N, M, V = map(int, read().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    inputs = list(map(int, read().split()))
    graph[inputs[0]].append(inputs[1])
    graph[inputs[1]].append(inputs[0])

for i in graph:
    i.sort()

def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for node in graph[start]:
        if not visited[node]:
            dfs(node)
            
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (N+1)
dfs(V)
print()

visited = [False] * (N+1)
bfs(V)
