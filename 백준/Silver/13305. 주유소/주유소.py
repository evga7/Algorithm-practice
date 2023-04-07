import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=b[0]
res=0
for i,cur in enumerate(a):
    res+=c*cur
    c=min(c,b[i+1])
print(res)