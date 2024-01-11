import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
res=0
c=[-1 for _ in range(11)]
for i in range(N):
    a,b=map(int,input().split())
    if c[a]!=-1 and c[a]!=b:
        res+=1
    c[a] = b
print(res)