import sys
def input():
    return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
left=0
right=0
s=0
l=0
dp=[0 for _ in range(N+1)]
while True:
    if s>=M:
        if left-1>=0:
            l=max(l,dp[left-1])
        dp[right-1]=max(dp[right-1],s+l-M)
        s-=a[left]
        left+=1
    else:
        if right==N:
            break
        s+=a[right]
        right+=1
print(max(dp))

