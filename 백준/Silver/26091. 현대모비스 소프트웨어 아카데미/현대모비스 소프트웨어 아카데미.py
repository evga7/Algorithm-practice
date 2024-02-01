import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,M=map(int,input().split())
a=list(map(int,input().split()))
left=0
right=N-1
a.sort()
res=0
while left<right:
    if a[right]+a[left]>=M:
        right-=1
        res+=1
    left+=1
print(res)