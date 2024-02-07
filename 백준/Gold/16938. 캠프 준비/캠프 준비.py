import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,L,R,X=map(int,input().split())
a=list(map(int,input().split()))
res=0
visited=[0 for _ in range(N)]
def go(idx,s,mi,mx,cnt):
    if L<=s<=R and (mx-mi)>=X and cnt>=2:
        global res
        res+=1
    if idx==N or s>R:
        return
    for i in range(idx,N):
        if visited[i]:continue
        visited[i]=1
        go(i+1,s+a[i],min(mi,a[i]),max(mx,a[i]),cnt+1)
        visited[i]=0
        
go(0,0,987654321,0,0)
print(res)
    