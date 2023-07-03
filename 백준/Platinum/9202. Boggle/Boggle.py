dx=[-1,-1,-1,0,1,1,1,0]
dy=[-1,0,1,1,1,0,-1,-1]
from collections import *
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import sys
def input(): return sys.stdin.readline().rstrip()
T=int(input())
st=set()
st3=set()
for i in range(T):
    s=input()
    st.add(s)
temp=input()
M=int(input())
def point(s):
    l=len(s)
    if 1<=l<=2:
        return 0
    elif 3<=l<=4:
        return 1
    elif l==5:
        return 2
    elif l==6:
        return 3
    elif l==7:
        return 5
    elif l==8:
        return 11
def go(x,y,cnt,s):
    if s in st:
        st2.add(s)
    if cnt==8:
        return
    for i in range(8):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,4,4) and not visited[n_x][n_y]:
            visited[n_x][n_y]=1
            go(n_x,n_y,cnt+1,s+a[n_x][n_y])
            visited[n_x][n_y]=0

while M:
    visited=[[0 for _ in range(4)] for _ in range(4)]
    st2 = set()
    res1=0
    M-=1
    a=[list(input()) for _ in range(4)]

    for i in range(4):
        for j in range(4):
            visited[i][j]=1
            go(i,j,1,a[i][j])
            visited[i][j]=0
    if M:
        temp=input()
    res2=''
    for cur in st2:
        res1+=point(cur)
        if len(cur)>=len(res2):
            if len(cur)==len(res2):
                res2=min(res2,cur)
            else:
                res2=cur

    print(res1,res2,len(st2))