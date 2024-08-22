import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N,M=map(int,input().split())
left=0
right=M

a=[list(map(int,input().split())) for _ in range(N)]
s=0
for x,y in a:
    s+=x
    if s>M:
        print(-1)
        exit(0)
while left<=right:
    mid=left+right>>1
    s=0
    f=1
    for x,y in a:
        if x>mid:
            f=0
            break
        s+=min(y,mid)
    if f and s>=M:
        right=mid-1
    else:
        left=mid+1
if left>M:
    left=-1
print(left)