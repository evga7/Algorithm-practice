import sys
sys.setrecursionlimit(100000)
def input():
    return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
res=987654321
def go(idx,back,s,cnt):
    if idx==N:
        global res
        res=min(res,cnt)
        return 0
    if not s:
        go(idx + 1, a[idx], back-a[idx], cnt)
        go(idx + 1, a[idx] + 1, back-(a[idx]+1), cnt + 1)
        go(idx + 1, a[idx] - 1, back-(a[idx]-1), cnt + 1)
    else:
        if back-a[idx] == s:
            go(idx+1,a[idx],s,cnt)
        elif back-(a[idx]-1)==s:
            go(idx+1,a[idx]-1,s,cnt+1)
        elif back-(a[idx]+1)==s:
            go(idx+1,a[idx]+1,s,cnt+1)
go(1,a[0],0,0)
go(1,a[0]-1,0,1)
go(1,a[0]+1,0,1)
if res==987654321:
    res=-1
print(res)