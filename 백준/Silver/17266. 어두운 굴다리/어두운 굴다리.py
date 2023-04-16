import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
M=int(input())
arr=list(map(int,input().split()))
arr.sort()
res=0
res=max(res,arr[0]-0,N-arr[M-1])
for i in range(1,M):
    res=max(res,(arr[i]-arr[i-1]+1)//2)
print(res)