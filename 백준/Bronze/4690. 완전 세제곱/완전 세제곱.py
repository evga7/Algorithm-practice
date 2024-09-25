from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
#dx=[0,1,0,-1,-1,-1,1,1]
#dy=[1,0,-1,0,-1,1,1,-1]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
g=defaultdict(int)
for i in range(3,101):
    for j in range(2,i):
        for k in range(j+1,i):
            for l in range(k+1,i):
                a,b,c=pow(j,3),pow(k,3),pow(l,3)
                if pow(i,3)==(a+b+c):
                    print("Cube = %d, Triple = (%d,%d,%d)"%(i,j,k,l))