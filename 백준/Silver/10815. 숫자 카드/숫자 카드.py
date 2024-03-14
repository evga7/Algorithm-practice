import sys
import bisect
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=set(map(int,input().split()))
M=int(input())
b=list(map(int,input().split()))
for cur in b:
    if cur in a:
        print(1,end=' ')
    else:
        print(0,end=' ')