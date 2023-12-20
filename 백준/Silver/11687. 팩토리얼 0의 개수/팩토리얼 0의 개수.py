import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
def chk(num):
    cnt=0
    while num:
        cnt+=num//5
        num//=5
    return cnt
left=0
right=int(1e9)
res=right
while left<=right:
    mid=left+right>>1
    cnt=0
    if chk(mid)>=N:
        right=mid-1
        res = min(res, mid)
    else:
        left=mid+1
    
if chk(res)==N:
    print(res)
else:
    print(-1)