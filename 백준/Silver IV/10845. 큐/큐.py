from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
q=deque()
for i in range(N):
    a=list(input().split())
    if a[0]=="push":
        q.append(a[1])
    elif a[0]=="pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif a[0]=="size":
        print(len(q))
    elif a[0]=="empty":
        if not q:
            print(1)
        else:
            print(0)
    elif a[0]=="front":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
    