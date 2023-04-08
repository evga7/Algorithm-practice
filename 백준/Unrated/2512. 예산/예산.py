import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
arr=list(map(int,input().split()))
M=int(input())
left=0
right=int(1e19)
res=right
m=max(arr)
while left<=right:
    mid=left+right>>1
    c=0
    for cur in arr:
        c+=min(cur,mid)
    if c<=M and m>=mid:
        left=mid+1
    else:
        right=mid-1

print(left-1)