from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
s1=list(input())
N=int(input())
s2=deque()
for i in range(N):
    a=list(input().split())
    if a[0]=='L':
        if s1:
            s2.appendleft(s1.pop())
    elif a[0]=='D':
        if s2:
            s1.append(s2.popleft())
    elif a[0]=='B':
        if s1:
            s1.pop()
    else:
        s1.append(a[1])
print(''.join(s1+list(s2)))