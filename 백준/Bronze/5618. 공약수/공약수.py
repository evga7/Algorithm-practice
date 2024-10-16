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
N=int(input())
a=list(map(int,input().split()))
st=set()
mx=max(a)
st.add(1)
for i in range(2,mx+1):
    f=1
    for cur in a:
        if cur%i:
            f=0
            break
    if f:
        st.add(i)
print(*sorted(list(st)))