import sys
from collections import *
def input(): return sys.stdin.readline().rstrip()
N=int(input())
g=[[0 for _ in range(62)] for _ in range(62)]
for i in range(N):
    s=input()
    a,b,c=s.split()
    if a==c:continue
    g[ord(a)-ord('A')][ord(c)-ord('A')]=1
for k in range(58):
    for i in range(58):
        for j in range(58):
            if i!=j and g[i][k] and g[k][j]:
                g[i][j]=1
v=[]
for i in range(58):
    for j in range(58):
        if g[i][j]:
            s2='%s => %s'%(chr(i+65),chr(j+65))
            v.append(s2)
print(len(v))
for cur in v:
    print(cur)