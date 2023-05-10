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
    m[(x,y)]+=1
res=0
for cur in a:
    x,y=cur[0],cur[1]
    s1=(x+A,y)
    s2=(x,y+B)
    s3=(x+A,y+B)
    if s1 in m and s2 in m and s2 in m:
        res+=min(m[s1],m[s2],m[s3])
print(res)