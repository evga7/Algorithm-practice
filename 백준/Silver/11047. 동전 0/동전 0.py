import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[int(input()) for _ in range(N)]
a.sort(reverse=True)
res=0
for cur in a:
    if M>=cur:
        cnt=M//cur
        M-=cnt*cur
        res+=cnt
print(res)