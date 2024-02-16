import sys
import math
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
v=[]
for i in range(N):
    v.append(M-a[i-1])
if v:
    s=v[0]
    for cur in v:
        s=math.gcd(s,cur)
print(s)