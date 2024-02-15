import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
for i in range(N):
    s=list(input().split())
    for cur in s:
        print(cur[::-1],end=' ')