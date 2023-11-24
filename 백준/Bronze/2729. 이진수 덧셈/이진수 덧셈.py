import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
while N:
    N-=1
    a,b=input().split()
    a=int(a,2)
    b = int(b, 2)
    print(bin(a+b)[2:])