import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
res=-987654321
s=0
for cur in a:
    s+=cur
    s=max(cur,s)
    res=max(res,s)
print(res)