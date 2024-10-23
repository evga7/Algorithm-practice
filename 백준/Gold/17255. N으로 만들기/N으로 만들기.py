from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
st=set()
s=input()
q=deque()
q.append((len(s),s,""))
res=0
while q:
    l,cur,t=q.popleft()
    if l==1:
        res+=1
        continue
    left = cur[1:]
    right=cur[:-1]
    if not t+left in st:
        st.add(t+left)
        q.append((l-1,left,t+left))
    if not t + right in st:
        st.add(t + right)
        q.append((l - 1, right, t + right))
print(res)