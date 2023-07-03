dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
from collections import *
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import sys
def input(): return sys.stdin.readline().rstrip()
def cov(s):
    return ord(s)-ord('A')
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
st=set()
q=deque()
res=0
q.append((0,0,1,1<<(cov(a[0][0]))))
while q:
    x,y,cost,bit=q.popleft()
    res=max(res,cost)
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M):
            chk_bit=cov(a[n_x][n_y])
            if not (bit & (1<<chk_bit)):
                n_bit=bit|(1<<chk_bit)
                if not (n_x,n_y,n_bit) in st:
                    q.append((n_x,n_y,cost+1,n_bit))
                    st.add((n_x,n_y,n_bit))
print(res)