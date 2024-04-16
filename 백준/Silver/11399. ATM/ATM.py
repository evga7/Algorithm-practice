import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
N=int(input())
a=list(map(int,input().split()))
res=0
s=0
a.sort()
for cur in a:
    res+=s
    s+=cur
    res+=cur
print(res)