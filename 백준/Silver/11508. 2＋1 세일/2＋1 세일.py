import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
cnt=0
res=0
a=[int(input()) for _ in range(N)]
a.sort(reverse=True)
for cur in a:
    cnt+=1
    if cnt==3:
        cnt=0
        continue
    res+=cur
print(res)