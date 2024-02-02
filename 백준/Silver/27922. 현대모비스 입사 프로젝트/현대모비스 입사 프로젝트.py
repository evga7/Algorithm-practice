import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[-1 for _ in range(N+1)]
q=[]
w=[]
e=[]
for i in range(N):
    q.append(a[i][0]+a[i][1])
    w.append(a[i][0]+a[i][2])
    e.append(a[i][1]+a[i][2])
q.sort(reverse=True)
w.sort(reverse=True)
e.sort(reverse=True)
r1,r2,r3=0,0,0
for i in range(M):
    r1+=q[i]
    r2+=w[i]
    r3+=e[i]
print(max(r1,r2,r3))