import sys
t = int(sys.stdin.readline().rstrip())
all_data = []
for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().rstrip().split())
    location = []
    for _ in range(k):
        data = list(map(int,sys.stdin.readline().rstrip().split()))
        location.append(data)
    
    # all_data.append(location)

