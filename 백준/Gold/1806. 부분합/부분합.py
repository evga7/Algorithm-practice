import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
res=int(1e20)
left,right=0,0
s=0
while left<N:
    if s<M and right<N:
        s+=a[right]
        right+=1
    else:
        if s>=M:
            res=min(res,right-left)
        s-=a[left]
        left+=1

if res==int(1e20):
    res=0
print(res)