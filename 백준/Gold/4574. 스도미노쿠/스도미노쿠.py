def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()


def find_idx(x,y):
    return ((x//3)*3) + (y//3)
m=defaultdict(int)
pos=1
f=0
def chk(x,y,num):
    if not col[x][num] and not row[y][num] and not idx[find_idx(x,y)][num]:
        return True
    return False
def go(cnt):
    global f
    if f:
        return
    if cnt==len(v):
        print('Puzzle %d'%pos)
        for i in range(9):
            for j in range(9):
                print(a[i][j],end='')
            print('')
        f=1
        return
    x,y=v[cnt][0],v[cnt][1]
    if a[x][y]:
        go(cnt+1)
    else:
        if is_inside(x,y+1,9,9) and not a[x][y+1]:
            for i in range(1,10):
                for j in range(1,10):
                    if i==j:continue
                    if (i, j) in st or (j, i) in st: continue
                    if chk(x,y,i) and chk(x,y+1,j):
                        go2(x,y,i,1)
                        go2(x, y+1, j,1)
                        st.add((i,j))
                        st.add((j,i))
                        go(cnt+1)
                        st.remove((i,j))
                        st.remove((j, i))
                        go2(x, y,i,0)
                        go2(x, y + 1,j,0)
        if is_inside(x+1, y, 9, 9) and not a[x+1][y]:
            for i in range(1, 10):
                for j in range(1, 10):
                    if i==j:continue
                    if (i, j) in st or (j, i) in st: continue
                    if chk(x, y, i) and chk(x+1, y, j):
                        go2(x, y, i,1)
                        go2(x+1, y, j,1)
                        st.add((i, j))
                        st.add((j, i))
                        go(cnt + 1)
                        st.remove((i, j))
                        st.remove((j, i))
                        go2(x, y, i,0)
                        go2(x+1, y, j,0)


for i in range(26):
    m[chr(65+i)]=i
def go2(x,y,num,op):
    if op==0:
        a[x][y]=0
    else:
        a[x][y]=num
    idx[find_idx(x,y)][num]=op
    col[x][num]=op
    row[y][num]=op
while True:
    N=int(input())
    st=set()
    if not N:
        break
    a = [[0 for _ in range(9)] for _ in range(9)]
    v = []
    row = [[0 for _ in range(10)] for _ in range(10)]
    col = [[0 for _ in range(10)] for _ in range(10)]
    idx = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(N):
        U,LU,V,LV=input().split()
        U,V=int(U),int(V)
        x1,y1=m[LU[0]],int(LU[1])-1
        x2, y2 = m[LV[0]], int(LV[1])-1
        a[x1][y1]=U
        a[x2][y2] = V
        st.add((U,V))
        st.add((V,U))
        go2(x1, y1, U,1)
        go2(x2, y2, V,1)
    b=input().split()
    for i in range(9):
        cur=b[i]
        x,y=m[cur[0]],int(cur[1])-1
        a[x][y]=i+1
        go2(x,y,i+1,1)
    for i in range(9):
        for j in range(9):
            if a[i][j]==0:
                v.append((i,j))
    go(0)
    pos+=1
    f=0