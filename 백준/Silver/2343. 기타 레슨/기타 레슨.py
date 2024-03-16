import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
left=0
right=int(1e19)
while left<=right:
    mid=left+right>>1
    c=0
    cnt=0
    f=0
    for cur in a:
        if cur>mid:
            f=1
            break
        if c+cur>mid:
            c=0
            cnt+=1
        c+=cur
    if c:
        cnt+=1
    if cnt<=M and not f:
        right=mid-1
    else:
        left=mid+1
print(left)