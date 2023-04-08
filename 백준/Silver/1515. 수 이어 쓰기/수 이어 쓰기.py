from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=deque(input())
i=0
while True:
    i+=1
    s=deque(str(i))
    idx=0
    while N and idx<len(s):
        if N[0]==s[idx]:
            N.popleft()
        idx+=1
    if not N:
        break
print(i)