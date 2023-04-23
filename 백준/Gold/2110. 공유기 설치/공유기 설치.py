import sys
dx=[0,0,1,-1,-1,1,1,-1]
dy=[1,-1,0,0,1,1,-1,-1]
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
left,right=0,int(2e20)
a.sort()
res=0
while left<=right:
    mid=left+right>>1
    c=1
    back=a[0]
    for i in range(1,N):
        if a[i]-back>=mid:
            c+=1
            back=a[i]
    if c<M:
        right=mid-1
    else:
        left=mid+1
print(left-1)