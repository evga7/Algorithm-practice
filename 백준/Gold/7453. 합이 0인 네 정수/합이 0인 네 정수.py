from collections import *
import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
A,B,C,D=[],[],[],[]
for i in range(N):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
m=defaultdict(int)
for i in range(N):
    for j in range(N):
        m[A[i]+B[j]]+=1
res=0
for i in range(N):
    for j in range(N):
        s=-(C[i]+D[j])
        if s in m:
            res+=m[s]
print(res)