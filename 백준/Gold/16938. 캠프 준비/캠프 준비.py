import sys
def input():
    return sys.stdin.readline().rstrip()
N,L,R,X=map(int,input().split())
a=list(map(int,input().split()))
res=0
def go(idx,mx,mi,cnt,s):
    if cnt>=2 and L<=s<=R and mx-mi>=X:
        global res
        res+=1
    if idx==N:
        return
    for i in range(idx,N):
        n_mx=max(mx,a[i])
        n_mi =min(mi, a[i])
        if s+a[i]<=R:
            go(i+1,n_mx,n_mi,cnt+1,s+a[i])
go(0,0,987654321,0,0)
print(res)