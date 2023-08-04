import sys
from collections import *
from functools import cmp_to_key
dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
s=input()
s2=input()
c1=Counter(s)
c2=Counter(s2)
res=0
for i in range(26):
    cur=chr(i+97)
    cnt1,cnt2=0,0
    cnt1=c1[cur]
    cnt2=c2[cur]
    res+=abs(cnt1-cnt2)
print(res)
