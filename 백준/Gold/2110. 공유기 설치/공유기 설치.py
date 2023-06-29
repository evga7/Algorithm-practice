import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
left=0
right=int(1e15)
a.sort()
while left<=right:
    mid=left+right>>1
    cnt=1
    back=a[0]
    for i in range(1,N):
        if a[i]-back>mid:
            cnt+=1
            back=a[i]
    if cnt>=M:
        left=mid+1
    else:
        right=mid-1
print(left)