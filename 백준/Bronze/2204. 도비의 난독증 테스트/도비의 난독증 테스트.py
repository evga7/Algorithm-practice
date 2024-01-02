import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
while True:
    N=int(input())
    if not N:
        break
    a=[]
    for i in range(N):
        s=input()
        a.append((str.lower(s),s))
    a.sort()
    print(a[0][1])
        