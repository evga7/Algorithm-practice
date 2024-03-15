import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
a.sort(key=lambda x:(x[0],x[1]))
for cur in a:
    print(cur[0],cur[1])