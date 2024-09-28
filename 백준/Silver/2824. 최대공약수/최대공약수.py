import heapq
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N=int(input())
a=list(map(int,input().split()))
A=a[0]
for i in range(1,N):
    A*=a[i]
M=int(input())
b=list(map(int,input().split()))
B=b[0]
for i in range(1,M):
    B*=b[i]
print(str(math.gcd(A,B))[-9:])