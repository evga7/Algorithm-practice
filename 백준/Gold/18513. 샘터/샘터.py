from collections import *
import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
st=set()
q=deque()
for cur in a:
    q.append((cur,0))
    st.add(cur)
res=0
while q:
    x,cost=q.popleft()
    for nxt in [x-1,x+1]:
        if not nxt in st:
            st.add(nxt)
            res+=cost+1
            q.append((nxt,cost+1))
        if len(st)==M+N:
            break
    if len(st) == M+N:
        break
print(res)