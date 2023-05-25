from collections import *
import heapq
dx=[0,0,1,-1]
dy=[1,-1,0,0]
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
st=set()
for i in range(M):
    num=int(input())
    st.add(num)
q=deque()
dist=[[987654321 for _ in range(501)] for _ in range(10001)]
q.append((0,1,0))
while q:
    cost,pos,speed=q.popleft()
    if pos==N:
        print(cost)
        exit(0)
    i=0
    for cur in (speed-1,speed,speed+1):
        nxt=pos+cur
        if cur>0 and nxt<=N and not nxt in st and dist[pos][cur]>cost+1:
            dist[pos][cur]=cost+1
            q.append((cost+1,nxt,cur))
        i+=1
print(-1)