import sys
import math
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
p=[0 for _ in range(1000001)]
def c():
    for i in range(2,int(math.sqrt(1000001))+1):
        if p[i]:continue
        for j in range(i*i,1000001,i):
            p[j]=1
c()
p[1]=1
N,M=map(int,input().split())
for i in range(N,M+1):
    if not p[i]:
        print(i)