import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
arr=[0 for _ in range(N)]
for i,cur in enumerate(a):
    cnt=0
    for j in range(N):
        if cnt==cur and arr[j]==0:
            arr[j]=i+1
            break
        if arr[j]==0:
            cnt+=1
print(*arr)