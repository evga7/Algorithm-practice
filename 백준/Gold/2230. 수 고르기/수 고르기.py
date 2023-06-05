import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
a.sort()
left=0
right=1
res=int(2e10)
while left<N and right<N:
    s=abs(a[right]-a[left])
    if s>=M:
        res=min(res,s)
        left+=1
    else:
        right+=1

print(res)