from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
m=defaultdict(list)
N,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for cur in a:
    for cur2 in b:
        m[cur2].append(cur*cur2)
r=[]
for cur in m:
    m[cur].sort(reverse=True)
    r.append((m[cur][0],cur))
r.sort(reverse=True)
print(r[M][0])