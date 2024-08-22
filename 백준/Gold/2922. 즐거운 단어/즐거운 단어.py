from collections import *
import bisect
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
s=list(input())
res=0
l=len(s)
m=defaultdict(int)
l_cnt=0
cnt=0
for i,cur in enumerate(s):
    if cur=='L':
        l_cnt=1
    if cur=='_':
        m[cnt]=i
        cnt+=1
def chk(c):
    if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
        return 1
    return 0
def go(idx,c,l_c):
    if idx==cnt:
        for i in range(2,l):
            if chk(s[i-2]) and chk(s[i-1]) and chk(s[i]):
                return
            elif not chk(s[i-2]) and not chk(s[i-1]) and not chk(s[i]):
                return
        global res
        if l_c:
            res+=c
        return
    i=m[idx]
    s[i]='A'
    go(idx+1,c*5,l_c)
    s[i] = 'B'
    go(idx + 1, c * 20,l_c)
    go(idx + 1, c, 1)
go(0,1,l_cnt)
print(res)