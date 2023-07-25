from collections import *
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
m=defaultdict(int)
for i in range(N):
    s=input()
    m[s]+=1
res=0
res_v=[]
for i in range(M):
    s=input()
    if s in m:
        res+=1
        res_v.append(s)
res_v.sort()
print(res)
for cur in res_v:
    print(cur)