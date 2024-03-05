from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
T=int(input())

while T:
    T-=1
    res = 987654321
    res2 = ''
    A,B=map(int,input().split())
    q=deque()
    q.append((0,A,""))
    visited=[0 for _ in range(10001)]
    visited[A]=1
    while q:
        cost,cur,op=q.popleft()
        if res<cost:continue
        if cur==B:
            if res>cost:
                res=cost
                res2=op
        if not visited[(cur*2)%10000]:
            visited[(cur*2)%10000]=1
            q.append((cost+1,(cur*2)%10000,op+'D'))
        n_sub=(cur-1)%10000
        if not visited[n_sub]:
            visited[n_sub]=1
            q.append((cost+1,n_sub,op+'S'))
        s_cur=str(cur)
        n_L=((cur%1000)*10)+(cur//1000)
        if not visited[n_L]:
            visited[n_L]=1
            q.append((cost + 1, n_L, op + 'L'))
        n_R=((cur%10)*1000)+(cur//10)
        if not visited[n_R]:
            visited[n_R]=1
            q.append((cost + 1, n_R, op + 'R'))
    print(res2)