import sys
from collections import *
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(input().split())
a.sort()
v=[]
st=set()
st.add('a')
st.add('e')
st.add('i')
st.add('o')
st.add('u')
visited=[0 for _ in range(M)]
def chk():
    f1=0
    f2=0
    for cur in v:
        if cur in st:
            f1+=1
        else:
            f2+=1
    if f1 and f2>1:
        return True
    return False
def go(idx,cnt):
    if cnt==N:
        if chk():
            print(''.join(v))
        return
    for i in range(idx,M):
        if visited[i]:continue
        visited[i]=1
        v.append(a[i])
        go(i+1,cnt+1)
        visited[i]=0
        v.pop()
go(0,0)