import sys
import heapq
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N,K=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
b=[int(input()) for _ in range(K)]
a.sort(key=lambda x:(x[0],-x[1]))
b.sort()
idx=0
q=[]
res=0
for cur in b:
    while idx<N and cur>=a[idx][0]:
        heapq.heappush(q,-a[idx][1])
        idx+=1
    if q:
        res-=heapq.heappop(q)
print(res)