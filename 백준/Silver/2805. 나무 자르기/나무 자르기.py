import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
left=0
right=int(1e10)
while left<=right:
    mid=left+right>>1
    cnt=0
    for cur in a:
        cnt+=max(0,cur-mid)
    if cnt>=M:
        left=mid+1
    else:
        right=mid-1
print(left-1)