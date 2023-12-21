import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
res=int(1e9)
def go(cnt,idx,c,d):
    if idx==N:
        global res
        if cnt:
            res=min(abs(c-d),res)
        return
    go(cnt,idx+1,c,d)
    go(cnt+1,idx+1,c*a[idx][0],d+a[idx][1])
go(0,0,1,0)
print(res)