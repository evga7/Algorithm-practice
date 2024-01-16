import sys
import math
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
for i in range(N):
    a,b=map(int,input().split())
    print((a*b)//math.gcd(a,b))