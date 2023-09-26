import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
a,b=map(int,input().split())
if a==b:
    print(0)
    exit(0)
s=int((b-a)**0.5)
if s**2==(b-a):
    print(2*s-1)
else:
    z=(b-a)-s**2
    if (z<=s):
        print(2*s)
    else:
        print(2*s+1)
