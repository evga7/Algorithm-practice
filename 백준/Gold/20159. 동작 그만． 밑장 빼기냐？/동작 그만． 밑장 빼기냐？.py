import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=list(map(int,input().split()))
res=0
s=0
for i in range(0,N,2):
    s+=a[i]
res=s
num=res
for i in range(N-1,0,-2):
    num+=a[i]
    num-=a[i-1]
    res=max(res,num)
num=s
for i in range(N-2,1,-2):
    num+=a[i-1]
    num-=a[i]
    res=max(res,num)
print(res)