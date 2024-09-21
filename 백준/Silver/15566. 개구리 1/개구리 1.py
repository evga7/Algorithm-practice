from collections import *
import sys

sys.setrecursionlimit(100000)


def input(): return sys.stdin.readline().rstrip()


MAX = sys.maxsize
MOD = int(1e9)


def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
g = defaultdict(int)
g2=defaultdict(set)
N, M = map(int, input().split())
a = [0]+[list(map(int, input().split())) for _ in range(N)]
b = [0]+[list(map(int, input().split())) for _ in range(N)]
v=[list(map(int,input().split())) for _ in range(M)]

f = 0
res_v = [0 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
c = [0 for _ in range(N+1)]
st=set()
cnt=0
for i in range(1,N+1):
    x,y=b[i]
    if x==y:continue
    else:
        g2[i+1].add(x)
        g2[i+1].add(y)
def chk():
    for s,e,op in v:
        op-=1
        if a[c[s]][op]!=a[c[e]][op]:
            return False
    return True
def go(cnt):
    temp=""
    for cur in c:
        temp+=str(cur)
    if temp in st:
        return
    st.add(temp)
    global f
    if f:
        return
    if cnt==N+1:
        if chk():
            global res_v
            res_v=c[:]
            f=1
        return
    for nxt in b[cnt]:
        if not c[nxt]:
            c[nxt]=cnt
            go(cnt+1)
            c[nxt]=0
go(1)
if f:
    print("YES")
    print(*res_v[1:])
else:
    print("NO")