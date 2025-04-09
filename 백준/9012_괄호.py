import sys

def is_vps(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:  # 스택이 비어있는데 ')'가 나오면 올바르지 않은 괄호열
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"  # 스택이 비어있으면 올바른 괄호열

n = int(sys.stdin.readline().strip())  # 입력 개수
for _ in range(n):
    print(is_vps(sys.stdin.readline().strip()))
