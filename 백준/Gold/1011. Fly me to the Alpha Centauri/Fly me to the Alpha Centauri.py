import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
T=int(input())
def solve(N):
    location = 0
    middle = N // 2
    count = 0
    max_speed = 1

    while location < middle:
        location += max_speed
        max_speed += 1
        count += 1

    rest = N - location
    speed = 1
    while rest > 0:
        rest -= speed
        count += 1
        if speed < max_speed - 1:
            speed += 1

    return count
while T:
    T-=1
    a,b=map(int,input().split())
    print(solve(b-a))