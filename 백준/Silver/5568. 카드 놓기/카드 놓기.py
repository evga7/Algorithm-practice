import sys
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
N=int(input())
K=int(input())
a=[int(input()) for _ in range(N)]
st=set()
c=[0 for _ in range(N+1)]
def go(idx,cnt,num):
    if cnt==K:
        st.add(num)
        return
    if idx==N:
        return
    for i in range(N):
        if c[i]:continue
        c[i]=1
        go(idx+1,cnt+1,num+str(a[i]))
        c[i]=0
go(0,0,"")
print(len(st))