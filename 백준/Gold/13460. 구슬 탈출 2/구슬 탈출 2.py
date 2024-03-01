dx = [-1,1,0,0]  # 위 아 오 왼
dy = [0,0,1,-1]
# dx = [-1,-2,-2,-1,1,2,2,1]  # 오 왼 위 아
# dy = [-2,-1,1,2,2,1,-1,-2]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
def chk(rx,ry,bx,by):
    if not is_inside(rx,ry,N,M) and is_inside(bx,by,N,M):
        return True
    return False
q=[]
rsx,rsy,bsx,bsy=0,0,0,0
st=set()
for i in range(N):
    for j in range(M):
        if a[i][j]=='B':
            bsx,bsy=i,j
            a[i][j]='.'
        elif a[i][j]=='R':
            rsx,rsy=i,j
            a[i][j]='.'
q.append((0,rsx,rsy,bsx,bsy))
st.add((rsx,rsy,bsx,bsy))
def chk2(rx,ry,bx,by,pos):
    if pos==0:
        if rx>=bx:
            return 1
        else:
            return 0
    elif pos==1:
        if rx<bx:
            return 1
        else:
            return 0
    elif pos==2:
        if ry>=by:
            return 0
        else:
            return 1
    else:
        if ry<by:
            return 0
        else:
            return 1


def go(rsx,rsy,bsx,bsy,pos):
    r_flag=0
    b_flag=0
    rx,ry,bx,by=rsx,rsy,bsx,bsy
    op=chk2(rx,ry,bx,by,pos)
    if op==1:
        while True:
            n_bx = bx + dx[pos]
            n_by = by + dy[pos]
            if is_inside(n_bx, n_by, N, M) and (a[n_bx][n_by] == '.' or a[n_bx][n_by]=='O'):
                bx, by = n_bx, n_by
                if a[bx][by] == 'O':
                    b_flag = 1
                    break
            else:
                break

        while True:
            n_rx = rx + dx[pos]
            n_ry = ry + dy[pos]
            if is_inside(n_rx, n_ry, N, M) and (a[n_rx][n_ry] == '.' or a[n_rx][n_ry]=='O') and (n_rx!=bx or n_ry!=by):
                if a[n_rx][n_ry]=='.' and n_rx==bx and n_ry==by:
                    break
                rx, ry = n_rx, n_ry
                if a[rx][ry] == 'O':
                    r_flag = 1
                    break
            else:
                break
    else:
        while True:
            n_rx = rx + dx[pos]
            n_ry = ry + dy[pos]
            if is_inside(n_rx, n_ry, N, M) and (a[n_rx][n_ry] == '.' or a[n_rx][n_ry]=='O'):
                rx, ry = n_rx, n_ry
                if a[rx][ry] == 'O':
                    r_flag = 1
                    break
            else:
                break
        while True:
            n_bx = bx + dx[pos]
            n_by = by + dy[pos]
            if is_inside(n_bx, n_by, N, M) and (a[n_bx][n_by] == '.' or a[n_bx][n_by]=='O'):
                if a[n_bx][n_by]=='.' and n_bx==rx and n_by==ry:
                    break
                bx, by = n_bx, n_by
                if a[bx][by] == 'O':
                    b_flag = 1
                    break
            else:
                break


    if r_flag:
        rx,ry=-1,-1
    if b_flag:
        bx,by=-1,-1
    return (rx,ry,bx,by)

while q:
    cost,rx,ry,bx,by=heapq.heappop(q)
    if cost>=10:continue
    for i in range(4):
        n_rx,n_ry,n_bx,n_by=go(rx,ry,bx,by,i)
        if n_rx==-1 and n_bx!=-1:
            print(cost+1)
            exit(0)
        if not (n_rx,n_ry,n_bx,n_by) in st:
            st.add((n_rx,n_ry,n_bx,n_by))
            heapq.heappush(q,(cost+1,n_rx,n_ry,n_bx,n_by))
print(-1)