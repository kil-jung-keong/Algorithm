import sys 

read = sys.stdin.readline 
N = int(read())

def is_group(word):
    group_checker = True 
    word_list = list(word)
    cnt_dic = {}
    for w in list(set(word_list)):
        cnt_dic[w] = []
    for idx,w in enumerate(word_list):
        cnt_dic[w].append(idx)
    for word,cnt in cnt_dic.items():
        cnt.sort()
        if len(cnt) > 1:
            for i in range(len(cnt)-1):
                if cnt[i+1] - cnt[i] != 1:
                    group_checker = False
    return group_checker

result = 0
for _ in range(N):
    word = read().rstrip()
    if is_group(word):
        result += 1

print(result)
    
