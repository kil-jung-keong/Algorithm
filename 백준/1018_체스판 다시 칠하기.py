import sys 

read = sys.stdin.readline 
N, M = map(int,read().split())
chess_map = []
for _ in range(N):
    chess_map.append(read().rstrip())

windows = []
for i in range(N-7):
    window_xs = chess_map[i:i+8]
    for j in range(M-7):
        window = [w[j:j+8] for w in window_xs]
        windows.append(window)

answer1 = []
for i in range(8):
    if i % 2 == 0:
        answer1.append('WBWBWBWB')
    else:
        answer1.append('BWBWBWBW')
answer2 = []
for i in range(8):
    if i % 2 == 0:
        answer2.append('BWBWBWBW')
    else:
        answer2.append('WBWBWBWB')

result = sys.maxsize
for window in windows:
    cnt_1 = 0
    cnt_2 = 0
    for i in range(8):
        for j in range(8):
            if window[i][j] != answer1[i][j]:
                cnt_1 += 1
            if window[i][j] != answer2[i][j]:
                cnt_2 += 1
    result = min(cnt_1,cnt_2,result)
            
print(result)
