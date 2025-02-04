import bisect
import heapq
import sys
from collections import *
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
N,K=map(int,input().split())
st=set(map(int,input().split()))
q=deque()
for cur in st:
    q.append((cur,0))
res=0
while q:
    cur,cost=q.popleft()
    for nxt in [cur-1,cur+1]:
        if nxt in st :continue
        st.add(nxt)
        q.append((nxt,cost+1))
        res+=cost+1
        if len(st)==N+K:
            break
    if len(st) == N + K:
        break
print(res)
