import sys
m = int(sys.stdin.readline().rstrip()) # rstrip : 인자로 전달된 문자를 string의 오른쪽에서 제거
a = list(map(int,sys.stdin.readline().rstrip().split()))
n = int(sys.stdin.readline().rstrip())
b = list(map(int,sys.stdin.readline().rstrip().split()))
# 이진 탐색을 위한 정렬
a.sort()

def binary_search(a,x):
    left, right = 0, len(a)-1
    while left <= right:
        mid = (left+right) // 2
        if x == a[mid]:
            return 1
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return 0

def solution(a, b):
    res = []
    for x in b:
        num = binary_search(a,x)
        res.append(num)
    return res
res = solution(a,b)
for x in res:
    print(x)
    
