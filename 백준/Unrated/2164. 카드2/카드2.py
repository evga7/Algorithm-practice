from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
q=[i+1 for i in range(N)]
q=deque(q)
while len(q)>1:
    q.popleft()
    q.append(q.popleft())
print(*q)