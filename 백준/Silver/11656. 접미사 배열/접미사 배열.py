from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
s=deque(input())
res=[]
while s:
    res.append(''.join(s))
    s.popleft()
res.sort()
for cur in res:
    print(cur)