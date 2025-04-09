import sys
sys.setrecursionlimit(500000)
m = int(sys.stdin.readline().rstrip())
a = list(map(int,sys.stdin.readline().rstrip().split()))
n = int(sys.stdin.readline().rstrip())
b = list(map(int,sys.stdin.readline().rstrip().split()))

a.sort()

def binary_search(a,x):
    count = 0
    left,right = 0, len(a)-1
    if x in a:
        while x in a:
            mid = (left+right) // 2
            if x == a[mid]:
                count += 1
                a.remove(x)
            elif x < a[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return count
    else:
        return 0
    

def solution(a,b):
    result = []
    for x in b:
        count = binary_search(a,x)
        result.append(count)
    return result

result = solution(a,b)
print(' '.join(str(x) for x in result))
