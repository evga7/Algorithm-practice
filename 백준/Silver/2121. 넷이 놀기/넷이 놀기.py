from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
A,B=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
m=defaultdict(int)
a.sort()
for cur in a:
    x,y=cur[0],cur[1]
    s=str(x)+' '+str(y)
    m[s]+=1
res=0
for cur in a:
    x,y=cur[0],cur[1]
    s1=str(x+A)+' '+str(y)
    s2=str(x) + ' ' + str(y+B)
    s3=str(x+A) + ' ' + str(y+B)
    ss1 = str(x) + ' ' + str(y+A)
    ss2 = str(x+B) + ' ' + str(y)
    ss3 = str(x + B) + ' ' + str(y + A)
    if s1 in m and s2 in m and s2 in m:
        res+=min(m[s1],m[s2],m[s3])
print(res)