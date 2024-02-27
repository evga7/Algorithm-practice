import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
res=0
def go(idx,s,cnt):
    if idx==N:
        global res
        if s==M and cnt:
            res+=1
        return
    go(idx+1,s+a[idx],cnt+1)
    go(idx+1,s,cnt)
go(0,0,0)
print(res)