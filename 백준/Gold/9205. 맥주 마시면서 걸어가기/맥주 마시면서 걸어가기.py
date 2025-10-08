import bisect
import heapq
import itertools
import sys
from collections import *
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
def cal(idx,idx2):
    x,y=a[idx][0],a[idx][1]
    X,Y=a[idx2][0],a[idx2][1]
    return (abs(x-X)+abs(y-Y))<=1000

while T:
    T-=1
    N=int(input())
    a=[list(map(int, input().split())) for _ in range(N+2)]
    st=set()
    q=deque()
    q.append(0)
    flag=0
    while q:
        idx=q.popleft()
        x,y=a[idx][0],a[idx][1]
        if cal(idx,N+1):
            flag=1
            break
        for i in range(N+1):
            if i==idx:continue
            if cal(idx,i) and not (idx,i) in st:
                st.add((idx,i))
                q.append(i)
    if flag:
        print("happy")
    else:
        print("sad")





