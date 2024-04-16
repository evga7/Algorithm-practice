import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
res=MAX
a.sort()
left=0
right=1
while left<=right and right<N:
    s=a[right]-a[left]
    if s>=M:
        res=min(res,s)
        left+=1
    else:
        right+=1
print(res)