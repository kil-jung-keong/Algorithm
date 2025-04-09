import sys 

read = sys.stdin.readline 
cogwheel_state = []
for _ in range(4):
    cogwheel_state.append(list(map(int,read().rstrip())))

K = int(input())
turns = []
for _ in range(K):
    turns.append(list(map(int,read().split())))

def clockwise(wheel):
    new = [wheel[-1]]
    for w in wheel[:-1]:
        new.append(w)
    return new 

def counter_clockwise(wheel):
    new = []
    for w in wheel[1:]:
        new.append(w)
    new.append(wheel[0])
    return new

for turn in turns:
    # 맞닿는 톱니 위치 
    meets = [[None,cogwheel_state[0][2]],
    [cogwheel_state[1][6],cogwheel_state[1][2]],
    [cogwheel_state[2][6],cogwheel_state[2][2]],
    [cogwheel_state[3][6],None]]    
    # 안움직이면 0, 시계방향 1, 반시계방향 -1 로 저장
    move_or_not = [0] * 4    
    # 시작 톱니바퀴 회전 방향 저장
    move_or_not[turn[0]-1] = turn[1]
    # 왼쪽으로 전파
    for i in range(turn[0] - 1, 0, -1):
        if meets[i][0] != meets[i - 1][1]:
            move_or_not[i - 1] = -move_or_not[i]
        else:
            break

    # 오른쪽으로 전파
    for i in range(turn[0] - 1, 3):
        if meets[i][1] != meets[i + 1][0]:
            move_or_not[i + 1] = -move_or_not[i]
        else:
            break     
    for idx,mv in enumerate(move_or_not):
        if mv == 1:
            cogwheel_state[idx] = clockwise(cogwheel_state[idx])
        elif mv == -1:
            cogwheel_state[idx] = counter_clockwise(cogwheel_state[idx])      

score = 0

if cogwheel_state[0][0] == 1:
    score += 1 
if cogwheel_state[1][0] == 1:
    score += 2
if cogwheel_state[2][0] == 1:
    score += 4 
if cogwheel_state[3][0] == 1:
    score += 8 

print(score)




















