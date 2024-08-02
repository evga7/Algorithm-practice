import heapq
from collections import *
#sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

import math
import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
m=defaultdict(int)
st=set()
h=[]
l=[]
N=int(input())
for i in range(N):
    q,w=map(int,input().split())
    heapq.heappush(h,(-w,-q))
    heapq.heappush(l, (w, q))
    st.add(q)
    m[q]=w
M=int(input())
for i in range(M):
    t=input().split()
    q=t[0]
    w=int(t[1])
    if q=="add":
        e=int(t[2])
        heapq.heappush(h, (-e, -w))
        heapq.heappush(l, (e, w))
        m[w]=e
        st.add(w)
    elif q=="recommend":
        if w==-1:
            while l:
                cost,num=l[0]
                if cost==m[num]:
                    break
                heapq.heappop(l)
            print(num)
        else:
            while h:
                cost,num=h[0]
                cost,num=-cost,-num
                if cost==m[num]:
                    break
                heapq.heappop(h)
            print(num)
    elif q=="solved":
        st.remove(w)
        del m[w]