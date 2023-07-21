from collections import *
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import sys
def input(): return sys.stdin.readline().rstrip()
T=int(input())
while T:
    T-=1
    s=input().split()
    m=defaultdict(list)
    for i,cur in enumerate(s):
        m[cur].append(i)
    while True:
        ss=input()
        ss2=ss.split()
        if ss=="what does the fox say?":
            break
        else:
            for cur in ss2:
                if cur in m:
                    del m[cur]
    res_v=[]
    for cur in m:
        for cur2 in m[cur]:
            res_v.append((cur2,cur))
    res_v.sort()
    for cur in res_v:
        print(cur[1],end=' ')