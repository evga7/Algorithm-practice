import sys
import math
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
g=math.gcd(N,M)
print(g)
print(N*M//g)