import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,M=map(int,input().split())
a=list(map(int,input().split()))
left=0
right=int(1e12)
while left<=right:
    mid = left+right>>1
    cnt=0
    for cur in a:
        cnt+=mid//cur
        
    if cnt>=M:
        right=mid-1
    else:
        left=mid+1
print(left)