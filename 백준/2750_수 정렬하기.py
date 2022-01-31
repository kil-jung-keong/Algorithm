import sys
n = int(sys.stdin.readline().rstrip())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline().rstrip()))
def sorting(num):
    sorted_num = sorted(num)
    return sorted_num

sorted_num = sorting(num)
for i in range(n):
    print(sorted_num[i])
    