import sys
def input():
    return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
left=0
right=int(1e10)
res=right
while left<=right:
    mid=left+right>>1
    cnt=1
    mx=0
    mi=10001
    for cur in a:
        mi=min(mi,cur)
        mx=max(mx,cur)
        if mx-mi>=mid:
            cnt+=1
            mx=0
            mx=mi=cur
    if cnt<=M:
        right=mid-1
    else:
        left=mid+1
print(left-1)

