from collections import *
#sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
st=set()
A,B,N,M=map(int,input().split())
if A<B:
    A,B=B,A
q=deque()
q.append((0,N))
while q:
    cost,cur=q.popleft()
    if cur==M:
        print(cost)
        exit(0)
    for nxt in [cur*A,cur*B,cur+A,cur+B,cur-A,cur-B,cur-1,cur+1]:
        if 0<=nxt<=100000 and not nxt in st:
            st.add(nxt)
            q.append((cost+1,nxt))