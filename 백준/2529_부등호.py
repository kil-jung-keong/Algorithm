import sys 

read = sys.stdin.readline 
k = int(read().rstrip())
inequality = list(map(str, read().split()))

# 문자 부등호를 이용해서 값 비교하기 
def str2real(inequal, nums):
    for i in range(k):
        if inequal[i] == '<' and nums[i] >= nums[i+1]:
            return False
        if inequal[i] == '>' and nums[i] <= nums[i+1]:
            return False
    return True  

visited = [False] * 10
ex_nums = [i for i in range(10)]
answer_min = []
answer_max = []
found_min = False
found_max = False

def find_min(depth):
    global found_min 
    if found_min:
        return
    if depth == k + 1:
        if str2real(inequality, answer_min):
            print(''.join(map(str, answer_min)))
            found_min = True 
        return

    for i in range(10):
        if not visited[i]:
            visited[i] = True
            answer_min.append(i)
            find_min(depth+1)
            visited[i] = False 
            answer_min.pop()

def find_max(depth):
    global found_max 
    if found_max:
        return
    if depth == k + 1:
        if str2real(inequality, answer_max):
            print(''.join(map(str, answer_max)))
            found_max = True 
        return

    for i in range(10):
        if not visited[i]:
            visited[i] = True
            answer_max.append(ex_nums[9-i])
            find_max(depth+1)
            visited[i] = False 
            answer_max.pop()

find_max(0)
visited = [False] * 10
find_min(0)
