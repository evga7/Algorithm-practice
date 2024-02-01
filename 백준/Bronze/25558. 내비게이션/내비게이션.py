import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
sx,sy,dx,dy=map(int,input().split())
res=1
m=int(1e15)
for i in range(N):
    s=0
    M=int(input())
    x,y=sx,sy
    for j in range(M):
        a,b=map(int,input().split())
        s+=abs(a-x)+abs(b-y)
        x,y=a,b
    s += abs(dx - x) + abs(dy - y)
    if m>s:
        m=s
        res=i+1
print(res)



