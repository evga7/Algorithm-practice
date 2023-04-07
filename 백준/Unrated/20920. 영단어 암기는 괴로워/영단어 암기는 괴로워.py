from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
m=defaultdict(int)
for i in range(N):
    s=input()
    if len(s)>=M:
        m[s]+=1
v=[]
for cur in m:
    v.append((m[cur],len(cur),cur))
v.sort(key=lambda x:(-x[0],-x[1],x[2]))
for cur in v:
    print(cur[2])