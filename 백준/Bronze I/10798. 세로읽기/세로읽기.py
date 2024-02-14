import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
a=[list(input()) for _ in range(5)]
m=0
for cur in a:
    m=max(m,len(cur))
    
for j in range(m):
    for i in range(5):
        if j>=len(a[i]):continue
        print(a[i][j],end='')