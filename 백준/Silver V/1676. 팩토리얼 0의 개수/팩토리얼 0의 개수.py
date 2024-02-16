import sys
import math
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
N=int(input())
res=0
while N:
    res+=N//5
    N//=5
print(res)