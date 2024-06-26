import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N=int(input())
a=list(map(int,input().split()))
a.sort()
res=0
c=0
for cur in a:
    c+=cur
    res+=c
print(res)