from collections import *
#sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


import sys
def input():return sys.stdin.readline().rstrip()
N=input()
q=deque()
st=set()
res=0
q.append((N,N,len(N)))
while q:
    cur,t,l=q.popleft()
    if l==1:
        res+=1
        continue
    left=cur[1:]
    right=cur[:l-1]
    if not t+left in st:
        st.add(t+left)
        q.append((left,t+left,l-1))
    if not t+right in st:
        st.add(t+right)
        q.append((right,t+right,l-1))
print(res)