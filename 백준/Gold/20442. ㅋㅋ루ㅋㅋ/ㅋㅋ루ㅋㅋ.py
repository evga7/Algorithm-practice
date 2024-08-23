from collections import *
import bisect
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
s=input()
res=s.count('R')
l=len(s)
l_s=[0 for _ in range(l)]
r_s=[0 for _ in range(l)]
R_s=[0 for _ in range(l+1)]
if s[0]=='K':
    l_s[0]=1
if s[l-1]=='K':
    r_s[l-1]=1
if s[0]=='R':
    R_s[0]=1
for i in range(1,l):
    l_s[i]=l_s[i-1]
    r_s[l-i-1]=r_s[l-i]
    R_s[i+1]=R_s[i]
    if s[i]=='K':
        l_s[i]+=1
    else:
        R_s[i+1]+=1
    if s[l-i-1]=='K':
        r_s[l-i-1]+=1
r_cnt=0
l_idx=-1
r_idx=-1
l_m=defaultdict(int)
r_m=defaultdict(int)
for i in range(l):
    if s[i]=='K':
        if not l_s[i] in l_m:
            l_m[l_s[i]]=i
    if s[l-i-1]=='K':
        if not r_s[l-i-1] in r_m:
            r_m[r_s[l-i-1]]=l-i-1
l_cnt=0
for i in range(l):
    if s[i]=='R':
        mi=min(l_s[i],r_s[i])
        if mi:
            l_idx=l_m[mi]
            r_idx = r_m[mi]
            res=max(res,(R_s[r_idx]-R_s[l_idx])+mi*2)
    elif s[i]=='K':
        l_cnt+=1
        r_idx=r_m[l_cnt]
        if i<r_idx and (R_s[r_idx]-R_s[i])>0:
            res=max(res,(R_s[r_idx]-R_s[i])+l_cnt*2)

print(res)