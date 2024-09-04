import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
s=input()
s2=input()
if s2 in s:
    print(1)
else:
    print(0)