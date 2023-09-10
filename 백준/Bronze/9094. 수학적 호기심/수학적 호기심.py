import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize

def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
T=int(input())

for _ in range(T):
    N,M=map(int,input().split())
    res=0
    for i in range(1,N):
        for j in range(i+1,N):
            div=i*j
            a=(pow(i, 2) + pow(j, 2) + M) // div
            b = (pow(i, 2) + pow(j, 2) + M) / div
            if a==b:
                res+=1
    print(res)