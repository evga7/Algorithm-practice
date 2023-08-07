import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
T=int(input())
arr=[0 for _ in range(1000001)]
arr[0]=1
def go():
    for i in range(1,1000001):
        num=i
        arr[i]+=arr[i-1]
        while num:
            if not num%10:
                arr[i]+=1
            num//=10
go()
while T:
    T-=1
    N,M=map(int,input().split())
    res=0
    if N==0:
        N+=1
        res=1
    res+=arr[M]-arr[N-1]
    print(res)