import math
from collections import *
import bisect
import re
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited=[0 for _ in range(10)]
c=[0 for _ in range(98766)]
c[1]=1
for i in range(2,int(math.sqrt(98766))+1):
    if c[i]:continue
    for j in range(i+i,98766,i):
        c[j]=1
v=[]
for i in range(2,98766):
    if not c[i]:
        v.append(i)
K,M=map(int,input().split())
res=0
l=len(v)
st=set()
st2=set()
MX=98765 // 10**(5-K)
for i in range(l):
    for j in range(i, l):
        c1=v[i] * v[j]
        c2=v[i] + v[j]
        if c1<=MX:
            st2.add(v[i] * v[j])
        if i==j:continue
        if c2<=MX:
            st.add(v[i]+v[j])
        else:
            break

def chk(num):
    f1 = num in st
    while num % M == 0:
        num //= M
    f2 = num in st2
    return f1 and f2
def go(cnt,num):
    if cnt==K:
        if chk(num):
            global res
            res+=1
        return
    for i in range(0,10):
        if cnt==0 and i==0:continue
        if visited[i]:continue
        visited[i]=1
        go(cnt+1,num*10+i)
        visited[i]=0
go(0,0)
print(res)
