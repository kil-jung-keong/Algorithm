import sys
n = int(sys.stdin.readline().rstrip())
# 각 시험장에 있는 응시자의 수
num_student = list(map(int, sys.stdin.readline().rstrip().split()))
# 총감독관이 감시할 수 있는 응시자수, 부감독관이 감시할 수 있는 응시자수
b, c = map(int, sys.stdin.readline().rstrip().split())

director = n
for student in num_student:
    student -= b
    if student > 0:
        if student % c == 0:
            director += (student // c)
        elif student % c != 0:
            director += (student // c)+1
print(director)





