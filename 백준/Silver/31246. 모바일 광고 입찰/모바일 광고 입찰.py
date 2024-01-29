import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
# map(int,input().split())
INF = sys.maxsize
N,M=map(int,input().split())
cnt=0
v=[]
for i in range(N):
    a,b=map(int,input().split())
    if a>=b:
        cnt+=1
    else:
        v.append(b-a)
    if cnt>=M:
        print(0)
        exit(0)
v.sort()
print(v[M-cnt-1])