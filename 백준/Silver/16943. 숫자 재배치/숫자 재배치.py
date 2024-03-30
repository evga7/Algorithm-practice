import sys
def input():
    return sys.stdin.readline().rstrip()
A,B=list(input().split())
l=len(A)
visited=[0 for _ in range(10)]
res=-1
b=int(B)
def go(idx,s):
    if s>b:
        return
    if idx==l:
        global res
        res=max(res,s)
        return
    for i in range(l):
        cur=int(A[i])
        if not s and not cur :continue
        if not visited[i]:
            visited[i]=1
            go(idx+1,s*10+cur)
            visited[i]=0
go(0,0)
print(res)

