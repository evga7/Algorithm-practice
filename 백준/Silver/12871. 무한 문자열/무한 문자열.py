import math
import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
s=input()
s2=input()
l=len(s)
l2=len(s2)
num=(l*l2)//math.gcd(l,l2)
if s*(num//l) == s2*(num//l2):
    print(1)
else:
    print(0)