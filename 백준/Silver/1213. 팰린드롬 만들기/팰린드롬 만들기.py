from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
s=input()
s=list(Counter(s).items())
s.sort()
res=""
cnt=0
res2=""
rm=""
for cur in s:
    c=cur[1]
    if c&1:
        rm=cur[0]
        cnt+=1
    if cnt>1:
        print("I'm Sorry Hansoo")
        exit(0)
    c//=2
    res+=(cur[0]*c)
    res2=(cur[0]*c)+res2
print(res+rm+res2)