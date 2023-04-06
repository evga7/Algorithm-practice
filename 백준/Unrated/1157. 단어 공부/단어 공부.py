from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
s=input()
s=str.upper(s)
c=Counter(s).most_common()
if len(c)>1 and c[0][1]==c[1][1]:
    res='?'
else:
    res=c[0][0]
print(res)