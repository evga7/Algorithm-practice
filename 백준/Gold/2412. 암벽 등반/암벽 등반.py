from collections import *
import heapq
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
m=defaultdict(int)
for cur in a:
    x,y=cur[0],cur[1]
    m[(x,y)]+=1
q=deque()
q.append((0,0,0))
st=set()
while q:
    x,y,cost=q.popleft()
    if y==M:
        print(cost)
        exit(0)
    for i in range(-2,3):
        for j in range(-2,3):
            if (x+i,y+j) in m and not (x+i,y+j) in st:
                q.append((x+i,y+j,cost+1))
                st.add((x+i,y+j))
print(-1)