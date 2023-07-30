import sys
from collections import *
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=set(map(int,input().split()))
b=[i for i in range(10)]
res=0
v=[]
def go(idx,cnt):
    if cnt==N:
        global res
        for cur in a:
            if not cur in v:
                return
        res+=1
        return
    for i in range(10):
        v.append(i)
        go(i,cnt+1)
        v.pop()
go(0,0)
print(res)