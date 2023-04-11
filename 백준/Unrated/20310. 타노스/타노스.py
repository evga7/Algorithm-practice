from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=input()
c=Counter(N)
for cur in c:
    c[cur]//=2
res=""
res+=c['0']*'0'
res+=c['1']*'1'
print(res)