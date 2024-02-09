import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
T=int(input())
idx=0

def find(x):
    if x==p[x]:
        return x
    p[x]=find(p[x])
    return p[x]
def uni(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        if x>y:
            p[y]=x
        else:
            p[x]=y
        return True
    return False
        
while T:
    T-=1
    idx+=1
    N=int(input())
    p = [i for i in range(N + 1)]
    K=int(input())
    for i in range(K):
        q,w=map(int,input().split())
        uni(q,w)
    M=int(input())
    print("Scenario "+str(idx)+":")
    for i in range(M):
        q,w=map(int,input().split())
        if find(q)==find(w):
            print(1)
        else:
            print(0)
    print('')