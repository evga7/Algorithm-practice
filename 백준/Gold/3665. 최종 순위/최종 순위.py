import sys
def input(): return sys.stdin.readline().rstrip()
T=int(input())
def go():
    q=[]
    res=[]
    for i in range(1,N+1):
        if not indegree[i]:
            q.append(i)
    while q:
        x=q.pop()
        res.append(x)
        for i in range(1,N+1):
            if g[x][i]:
                if indegree[i]:
                    indegree[i]-=1
                if not indegree[i]:
                    q.append(i)
    return res
while T:
    T-=1
    N=int(input())
    indegree=[0 for _ in range(N+1)]
    a=list(map(int,input().split()))
    g=[[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(i+1,N):
            g[a[j]][a[i]]=1
            indegree[a[i]]+=1
    M=int(input())
    for i in range(M):
        a,b=map(int,input().split()) #a가 b를 이김
        if g[a][b]: # b가 a를 이기고 있었음 (반대상황) a를 통해 b를 가야됨
            indegree[a]+=1
            indegree[b]-=1
            g[a][b]=0 #
            g[b][a]=1
        else: # a가 b를 이미 이기고 있었음
            indegree[b]+=1
            indegree[a]-=1
            g[b][a]=0
            g[a][b]=1

    r=go()
    if len(r)==N:
        print(*r[::-1])
    else:
        print("IMPOSSIBLE")