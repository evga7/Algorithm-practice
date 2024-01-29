import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
# map(int,input().split())
INF = sys.maxsize
N=int(input())
for i in range(N):
    num=int(input())
    if not (num+1)%(num%100):
        print("Good")
    else:
        print("Bye")