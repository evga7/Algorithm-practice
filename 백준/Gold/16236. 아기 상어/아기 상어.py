dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
import heapq


def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


import copy
from collections import *
import sys


# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()


N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
X, Y, P = 0, 0, 2
v = []
for i in range(N):
    for j in range(N):
        if a[i][j] == 9:
            X, Y = i, j
            a[i][j]=0
        elif a[i][j]:
            v.append((987654321, i, j,a[i][j]))


def swim(sx, sy, ex, ey, p):
    q = deque()
    q.append((0, sx, sy))
    visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visited[sx][sy] = 1
    while q:
        cost, x, y = q.popleft()
        if (x, y) == (ex, ey):
            return cost
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if is_inside(n_x, n_y, N, N) and not visited[n_x][n_y] and p >= a[n_x][n_y]:
                visited[n_x][n_y] = 1
                q.append((cost + 1, n_x, n_y))
    return 987654321


def chk(sx, sy, p):
    v2 = []
    for cur in v:
        cost, ex, ey,size = cur[0], cur[1], cur[2],cur[3]
        if not a[ex][ey]: continue
        if p > size:
            n_cost = swim(sx, sy, ex, ey, p)
            v2.append((n_cost, ex, ey,size))
        else:
            v2.append((987654321, ex, ey,size))
    v2.sort(key=lambda x: (x[0], x[1], x[2]))
    return v2


cnt = 0
res = 0
while True:
    v = chk(X, Y, P)
    if v and v[0][0] != 987654321:
        X, Y = v[0][1], v[0][2]
        a[X][Y] = 0
        cnt += 1
        res += v[0][0]
        if cnt == P:
            P += 1
            cnt = 0
    else:
        break

print(res)



