import sys
from collections import deque

# 입력
read = sys.stdin.readline
N, K = map(int, read().split())

# 방문 배열 생성
visited = [False] * (max(N,K) * 2 + 1)

def bfs(start, target):
    # 큐에 현재 위치와 이동 횟수를 저장
    queue = deque([(start, 0)])  # (현재 위치, 이동 횟수)
    visited[start] = True

    while queue:
        node, distance = queue.popleft()

        # 목표에 도달하면 이동 횟수 반환
        if node == target:
            return distance

        # 가능한 다음 위치 탐색
        for next_node in [node - 1, node + 1, node * 2]:
            # 범위를 벗어나지 않고 방문하지 않은 경우만 큐에 추가
            if 0 <= next_node < max(N,K) * 2 + 1 and not visited[next_node]:
                queue.append((next_node, distance + 1))
                visited[next_node] = True

# BFS 호출 및 결과 출력
result = bfs(N, K)
print(result)


        


