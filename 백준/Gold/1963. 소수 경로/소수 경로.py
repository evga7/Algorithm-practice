import heapq
import math

def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import copy
from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
T=int(input())
p=[0 for _ in range(10000)]
def c():
    for i in range(2,int(math.sqrt(10000))+1):
        if p[i]:continue
        for j in range(i+i,10000,i):
            p[j]=1
c()

while T:
    a,b=map(list,input().split())
    T-=1
    st=set()
    st.add(''.join(a))
    q=[]
    q.append((0,a))
    res=987654321
    while q:
        cost,cur=heapq.heappop(q)
        if cur==b:
            res=cost
            break
        for i in range(4):
            for j in range(10):
                if cur[i]==b[i] or int(cur[i])==j:continue
                temp=cur[:]
                temp[i]=str(j)
                t=''.join(temp)
                temp_int=int(t)
                if temp_int<1000 or p[temp_int] or t in st:continue
                st.add(t)
                heapq.heappush(q,(cost+1,temp))

    if res==987654321:
        print("Impossible")
    else:
        print(res)
