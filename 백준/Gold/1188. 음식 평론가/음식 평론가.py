import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
def gcd(a,b):
    while b:
        temp=b
        b=a%b
        a=temp
    return a
print(M-gcd(N,M))