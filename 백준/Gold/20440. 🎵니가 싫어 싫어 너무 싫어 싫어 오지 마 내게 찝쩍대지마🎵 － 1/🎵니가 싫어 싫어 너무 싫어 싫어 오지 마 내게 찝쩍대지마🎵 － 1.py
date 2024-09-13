from collections import *
import itertools
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
m=defaultdict(int)
for i in range(N):
    s,e=map(int,input().split())
    m[s]+=1
    m[e]-=1
cnt=0
res=0
res_s,res_e=0,0
for cur in sorted(list(m.keys())):
    cnt+=m[cur]
    if res<cnt:
        res=cnt
        res_s=cur
        res_e=0
    else:
        c=m[cur]
        if not res_e and c and cnt-m[cur]==res:
            res_e=cur
print(res)
print(res_s,res_e)