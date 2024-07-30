from collections import *
import bisect
# sys.setrecursionlimit(100000)
import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
m=defaultdict(int)
def cal(cur,nxt):
    cur_x,cur_y=m[cur]
    nxt_x, nxt_y = m[nxt]
    return abs(cur_x-nxt_x)+abs(cur_y-nxt_y)
for i,cur in enumerate(['q','w','e','r','t','y','u','i','o','p']):
    m[cur]=[0,i]
for i,cur in enumerate(['a','s','d','f','g','h','j','k','l']):
    m[cur]=[1,i]
for i,cur in enumerate(['z','x','c','v','b','n','m']):
    m[cur]=[2,i]
left,right=input().split()
m['left']=m[left]
m['right']=m[right]
s=input()
res=0
for cur in s:
    if cur in 'qwertasdfgzxcv':
        res+=cal(cur,'left')+1
        left=cur
        m['left']=m[cur]
    else:
        res+=cal(cur,'right')+1
        right=cur
        m['right']=m[cur]
print(res)