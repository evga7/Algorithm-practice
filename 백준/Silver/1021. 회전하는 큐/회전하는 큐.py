from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
arr=deque(i+1 for i in range(N))
res=0
for cur in a:
    idx=arr.index(cur)
    if idx<=len(arr)-idx:
        while arr[0]!=cur:
            arr.append(arr.popleft())
            res+=1
    else:
        while arr[0]!=cur:
            arr.appendleft(arr.pop())
            res+=1
    arr.popleft()
print(res)