from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
q=deque()
arr=[[] for _ in range(301)]
for i in range(N):
    l,n=input().split()
    l=int(l)
    f=0
    if q:
        for i,cur in enumerate(q):
            if l-10<=cur<=l+10 and len(arr[i])<M:
                arr[i].append((l,n))
                f=1
                break
    if not f:
        q.append(l)
        arr[len(q)-1].append((l,n))

for i,cur in enumerate(q):
    if len(arr[i])>=M:
        print('Started!')
    else:
        print('Waiting!')
    arr[i].sort(key=lambda x:x[1])
    for cur2 in arr[i]:
        print(cur2[0],cur2[1])