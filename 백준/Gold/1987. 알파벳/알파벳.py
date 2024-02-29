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
st=set()
def cal(c):
    return ord(c)-ord('A')
def go():
    q=deque()
    q.append((0,0,1<<cal(a[0][0]),1))
    r=0
    st.add((0,0,1<<cal(a[0][0])))
    while q:
        x,y,bit,cnt=q.popleft()
        r=max(r,cnt)
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M):
                n_bit=1<<cal(a[n_x][n_y])
                n_bit2=bit|n_bit
                if not bit & n_bit and not (n_x,n_y,n_bit2) in st:
                    q.append((n_x,n_y,n_bit2,cnt+1))
                    st.add((n_x,n_y,n_bit2))
    return r
        
print(go())