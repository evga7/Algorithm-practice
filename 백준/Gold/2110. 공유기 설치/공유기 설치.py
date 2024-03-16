import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
left=0
right=int(1e10)
a.sort()
while left<=right:
    mid=left+right>>1
    cnt=1
    back=a[0]
    for cur in a:
        if cur-back>=mid:
            back=cur
            cnt+=1
    if cnt>=M:
        left=mid+1
    else:
        right=mid-1
print(left-1)