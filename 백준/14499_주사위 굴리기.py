import sys
n, m, x, y, k = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))
orders = list(map(int,sys.stdin.readline().rstrip().split()))

# 주사위 초기화
dice = [0 for _ in range(6)]

# 동서남북 이동 - 주사위
def move_dice(dice,order):
    new_dice = dice.copy()
    if order == 4:
        new_dice[5] = dice[1]
        new_dice[4] = dice[5]
        new_dice[0] = dice[4]
        new_dice[1] = dice[0]
    elif order == 3:
        new_dice[1] = dice[5]
        new_dice[5] = dice[4]
        new_dice[4] = dice[0]
        new_dice[0] = dice[1]
    elif order == 1:
        new_dice[0] = dice[3]
        new_dice[2] = dice[0]
        new_dice[5] = dice[2]
        new_dice[3] = dice[5]
    elif order == 2:
        new_dice[3] = dice[0]
        new_dice[0] = dice[2]
        new_dice[2] = dice[5]
        new_dice[5] = dice[3]
    return new_dice
            
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 이동 - 좌표
def move_location(x,y,order):
    if order == 4:
        x += dx[1]
        y += dy[1]
    elif order == 3:
        x += dx[0]
        y += dy[0]
    elif order == 2:
        x += dx[2]
        y += dy[2]
    else:
        x += dx[3]
        y += dy[3]
    return x,y

# solution

for order in orders:
    x, y = move_location(x,y,order)
    if x < 0:
        x += 1
        continue
    elif x >= n:
        x -= 1
        continue
    elif y < 0:
        y += 1
        continue
    elif y >= m:
        y -= 1
        continue
    else:
        dice = move_dice(dice, order)
        if board[x][y] == 0:
            board[x][y] = dice[5] 
        else:
            dice[5] = board[x][y]
            board[x][y] = 0

        print(dice[0])



