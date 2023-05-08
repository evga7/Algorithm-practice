from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N,K=map(int,input().split())
a=deque(map(int,input().split()))
res=0
cnt=0
belt=deque(0 for _ in range(N*2))
while True:
    res+=1
    a.appendleft(a.pop())
    belt.appendleft(belt.pop())
    belt[N-1]=0
    for i in range(N-2,-1,-1):
        if belt[i]:
            if not belt[i+1] and a[i+1]:
                belt[i+1]=1
                belt[i]=0
                a[i+1]-=1
    belt[N-1]=0
    if a[0] and not belt[0]:
        a[0]-=1
        belt[0]=1
    c=a.count(0)
    if c>=K:
        break
print(res)