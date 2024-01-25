import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
#map(int,input().split())
INF=sys.maxsize
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
left=0
right=int(1e19)
while left<=right:
    mid=left+right>>1
    H=mid
    At=M
    for cur in a:
        op,A,T=cur[0],cur[1],cur[2]
        if H<=0:
            break
        if op==1:
            cnt=(T+At-1)//At
            H-=(cnt-1)*A
        else:
            At+=A
            H=min(H+T,mid)
    if H>0:
        right=mid-1
    else:
        left=mid+1
print(left)