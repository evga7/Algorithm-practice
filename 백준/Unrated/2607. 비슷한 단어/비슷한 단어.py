from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
s=input()
sc=Counter(s)
res=0
for i in range(N-1):
    s2=input()
    sc2=Counter(s2)
    if abs(len(s)-len(s2))>1:continue
    ss=0
    if len(s)>=len(s2):
        ss=sc-sc2
    else:
        ss=sc2-sc
    if len(ss)>1 or (ss and ss.most_common()[0][1]>1):continue
    res+=1
print(res)