import sys
import math
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
a,b=map(int,input().split())
c=[0 for _ in range(10000001)]
c[1]=1
def chk(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
def d():
    for i in range(2,int(math.sqrt(10000001))+1):
        for j in range(i*i,10000001,i):
            c[j]=1
            
d()
for i in range(a,min(b+1,10000001)):
    if not c[i] and chk(str(i)):
        print(i)
print(-1)