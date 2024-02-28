import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
res=0
def go(idx,s):
    if idx<3:
        global res
        res=max(res,s)
        return
    for i in range(1,len(a)-1):
        temp=a[i]
        cost=a[i-1]*a[i+1]
        del a[i]
        go(idx-1,s+cost)
        a.insert(i,temp)
go(N,0)
print(res)