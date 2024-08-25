from collections import *
import bisect
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
T=int(input())

def go():
    q=deque()
    global res
    for i in range(1,M+1):
        if not p[i]:
            q.append((i,1))
    while q:
        cur,cost=q.popleft()
        for nxt in g[cur]:
            p[nxt]-=1
            indegree[nxt][cost+1]-=1
            n_cost=cost
            if not indegree[nxt][cost+1]:
                n_cost+=1
                res=max(res,cost+1)
            if not p[nxt]:
                q.append((nxt,n_cost))


while T:
    T-=1
    g=defaultdict(list)
    K,M,P=map(int,input().split())
    p=[0 for _ in range(M+1)]
    indegree = [[2 for _ in range(32)] for _ in range(M+1)]
    for i in range(P):
        a,b=map(int,input().split())
        g[a].append(b)
        p[b]+=1
    res=1
    go()
    print(K,res)