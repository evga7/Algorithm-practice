import itertools
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
#dx=[0,1,0,-1]
#dy=[1,0,-1,0]
dx=[-1,-2,-2,-1,1,2,2,1]
dy=[-2,-1,1,2,2,1,-1,-2]
N,L,F=input().split()
a=[0,31,28,31,30,31,30,31,31,30,31,30,31]
b=list(itertools.accumulate(a))
N,F=int(N),int(F)
m2=defaultdict(int)
def cal(dd,hour,minute):
    return (dd * 24 * 60) + (hour * 60) + minute
def cal_minute(s,tt):
    y,m,d=s.split('-')
    m,d=int(m),int(d)
    dd=b[m-1]+d
    hour,minute=tt.split(':')
    hour,minute=int(hour),int(minute)
    return cal(dd,hour,minute)

s_day=L[:3]
s_hour,s_minu=L[4:].split(':')
p_minute=cal(int(s_day),int(s_hour),int(s_minu))
mp=defaultdict(int)
for i in range(N):
    t,m,kind,name=input().split()
    ss=kind+' '+name
    if not ss in mp:
        mp[ss]=cal_minute(t,m)
    else:
        temp=((cal_minute(t,m)-mp[ss])-p_minute)
        if temp>0:
            m2[name]+=temp*F
        del mp[ss]
res_v=[]
for cur in m2.keys():
    res_v.append((cur,m2[cur]))
res_v.sort()
if res_v:
    for x,y in res_v:
        print(x,y)
else:
    print(-1)
