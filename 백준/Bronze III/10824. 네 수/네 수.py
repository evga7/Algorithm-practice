import sys
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
a,b,c,d=input().split()
A=a+b
B=c+d
print(int(A)+int(B))