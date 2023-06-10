def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
from collections import *
import sys


def input(): return sys.stdin.readline().rstrip()


def go(op, dir):
    if op==1:
        if dir==2:
            dir+=1
        elif dir==3:
            dir-=1
    elif op==2:
        if dir==0:
            dir+=1
        elif dir==1:
            dir-=1
    elif op == 3:
        if dir == 0:
            dir += 3
        elif dir == 1:
            dir += 1
        elif dir == 2:
            dir -= 1
        elif dir == 3:
            dir += 1
    elif op == 4:
        dir += 2
    dir %= 4
    return dir


N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
v2 = []
for i in range(N):
    for j in range(M):
        if a[i][j] == 9:
            v2.append((i, j))
q = deque()
v=[[0 for _ in range(M)] for _ in range(N)]
for cur in v2:
    q.append((cur[0], cur[1]))
    v[cur[0]][cur[1]]=1
while q:
    sx, sy = q.popleft()
    for i in range(4):
        dir=i
        x,y=sx,sy
        while True:
            x += dx[dir]
            y += dy[dir]
            if not is_inside(x, y, N, M) or a[x][y] == 9 or dir==-1:
                break
            v[x][y] = 1
            if 1 <= a[x][y] <= 4:
                dir = go(a[x][y], dir)
res=0
for cur in v:
    res+=cur.count(1)
print(res)