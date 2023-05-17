from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
M=int(input())
head=0
g=[[] for _ in range(N)]
c=[0 for _ in range(N)]
for i,cur in enumerate(a):
    if cur==-1:
        head=i
        continue
    g[cur].append(i)
if head==M:
    print(0)
    exit(0)
q=deque()
q.append(head)
res=0
while q:
    cur=q.popleft()
    c=0
    for nxt in g[cur]:
        if nxt==M:continue
        c+=1
        q.append(nxt)
    if not c:
        res+=1
print(res)