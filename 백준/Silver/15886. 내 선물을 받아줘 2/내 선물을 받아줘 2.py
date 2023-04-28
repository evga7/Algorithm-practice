from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
v=[0 for _ in range(1001)]
N=int(input())
s=input()
res=0
def go(idx):
    q=deque()
    q.append(idx)
    while q:
        cur=q.popleft()
        if s[cur]=='E':
            if cur+1<N:
                v[cur+1]=1
                q.append(cur+1)
for i,cur in enumerate(s):
    if not v[i] and cur=='E':
        v[i]=1
        go(i)
        res+=1
print(res)