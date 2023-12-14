import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
a=list(map(int,input().split()))
left=0
right=int(1e7)
while left<=right:
    mid=left+right>>1
    cnt=0
    s=0
    for cur in a:
        s+=cur
        if s>=mid:
            s=0
            cnt+=1
    if cnt>=M:
        left=mid+1
    else:
        right=mid-1
print(left-1)