from collections import *
import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize

def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
N,M=map(int,input().split())
m=defaultdict(int)
for _ in range(N):
    b,c=map(int,input().split())
    m[c]=b

cnt=0
for i in range(M*2+1):
    if m[i]:
        cnt+=m[i]
res=cnt
left=0
right=M*2
while right<=2000000:
    cnt-=m[left]
    left+=1
    right+=1
    cnt+=m[right]
    res=max(res,cnt)
print(res)