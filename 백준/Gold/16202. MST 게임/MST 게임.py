import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
#dx = [0, -1, 1,0]
#dy = [1, 0, 0, -1]

def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]
def uni(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if x < y:
            p[y] = x
        else:
            p[x] = y
        return True
    return False
N,M,K=map(int,input().split())

v=[]
for i in range(M):
    s,e=map(int,input().split())
    v.append((i+1,s,e))
idx=0
while K:
    K-=1
    p = [i for i in range(N + 1)]
    res=0
    for i in range(idx,M):
        cost,s,e=v[i]
        if uni(s,e):
            res+=cost
    num=find(1)
    f=1
    for i in range(1,N+1):
        if num!=find(i):
            f=0
            break
    if f:
        print(res,end=' ')
    else:
        print(0,end=' ')
    idx+=1