import sys
def input():return sys.stdin.readline().rstrip()
T=int(input())
while T:
    T-=1
    N=int(input())
    q=[]
    arr=list(map(int,input().split()))
    d=[-1 for _ in range(N)]
    m=-1
    idx=-1
    for i in range(N-1,-1,-1):
        if m<arr[i]:
            m=arr[i]
            idx=i
        d[i]=idx
    res=0
    for i in range(N):
        res+=arr[d[i]]-arr[i]
    print(res)