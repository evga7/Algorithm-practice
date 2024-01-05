import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
c=[0 for _ in range(31)]
for i in range(28):
    num=int(input())
    c[num]=1
for i in range(1,31):
    if not c[i]:
        print(i)
