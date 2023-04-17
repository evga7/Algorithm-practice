from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
T=int(input())
while T:
    T-=1
    s=input()
    n=int(input())
    res1=987654321
    res2=0
    left=0
    right=0
    m2=defaultdict(list)
    while right<len(s):
        m2[s[right]].append(right)
        if len(m2[s[right]])>=n:
            cur=right
            before=m2[s[right]][-n]
            res1=min(res1,cur-before+1)
            res2=max(res2,cur-before+1)
        right+=1
    if not res2 or res1==987654321:
        print(-1)
    else:
        print(res1,res2)