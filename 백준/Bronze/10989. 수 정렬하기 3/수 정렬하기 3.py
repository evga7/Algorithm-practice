import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[0 for _ in range(10001)]
for i in range(N):
    num=int(input())
    a[num]+=1
for i in range(1,10001):
    if a[i]:
        num=a[i]
        for j in range(num):
            print(i)