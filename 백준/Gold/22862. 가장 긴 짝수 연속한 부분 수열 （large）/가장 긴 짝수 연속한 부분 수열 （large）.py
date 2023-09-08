import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize

def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
N,M=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
left=0
right=0
res=0
while right<N:
    if a[right]&1:
        cnt+=1
    while cnt>M:
        if a[left]&1:
            cnt-=1
        left+=1
    right+=1
    res=max(right-left-cnt,res)

print(res)