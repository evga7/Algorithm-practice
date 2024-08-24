import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,M=map(int,input().split())
a=set(list(map(int,input().split())))
b=set(list(map(int,input().split())))
print(len(a-b)+len(b-a))