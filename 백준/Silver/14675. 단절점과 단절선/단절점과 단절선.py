import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
# map(int,input().split())
INF = sys.maxsize
N=int(input())
l=[0 for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    l[a]+=1
    l[b]+=1
M=int(input())
for i in range(M):
    a,b=map(int,input().split())
    if a==1:
        if l[b]>=2:
            print("yes")
        else:
            print("no")
    else:
        print("yes")