import sys
import heapq
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
v=[0 for _ in range(11)]
arr=[0 for _ in range(11)]
arr[a[0]]=1
v[1]=1
ch=0
def go(cnt):
    global ch
    if ch:return
    if cnt==N:
        f=1
        for i in range(N):
            cnt=0
            c=a[arr[i]-1]
            for j in range(i):
                if arr[i]<arr[j]:
                    cnt+=1
            if cnt==c:continue
            else:
                f=0
                break
        if f:
            ch=1
            for i in range(N):
                print(arr[i],end=' ')
        return
    if arr[cnt]:
        go(cnt+1)
        return
    for i in range(2,N+1):
        if v[i]:continue
        arr[cnt]=i
        v[i]=1
        go(cnt+1)
        arr[cnt]=0
        v[i]=0

go(0)