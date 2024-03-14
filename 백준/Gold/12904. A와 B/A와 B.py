from collections import *
import sys


# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
S=deque(input())
T=deque(input())
f=0
while len(S)<len(T):
    if T[-1]=='A':
        T.pop()
    elif T[-1]=='B':
        T.pop()
        T.reverse()
    if S==T:
        f=1
        break
print(f)