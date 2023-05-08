from collections import *
import sys
import heapq
def input():return sys.stdin.readline().rstrip()
T=int(input())
while T:
    T-=1
    N,M=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    aa=deque()
    for i,cur in enumerate(a):
        aa.append((cur,i))
    for i,cur in enumerate(a):
        heapq.heappush(b,-cur)
    res=1
    while aa:
        top=heapq.heappop(b)
        while aa[0][0]!=-top:
            aa.append(aa.popleft())
        c=aa.popleft()
        if M==c[1]:
            break
        res+=1
    print(res)