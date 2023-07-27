import sys
def input(): return sys.stdin.readline().rstrip()
N,H=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
left=0
right=int(1e19)
while left<=right:
    mid=left+right>>1
    f=0
    HP=mid
    at=H
    for cur in arr:
        t,a,h=cur[0],cur[1],cur[2]
        if t==1:
            cnt=(h + (at - 1)) // at
            cnt-=1
            if HP<cnt*a:
                f=1
                break
            else:
                HP-=cnt*a
        else:
            at+=a
            HP=min(mid,HP+h)
    if f:
        left=mid+1
    else:
        right=mid-1
print(left+1)