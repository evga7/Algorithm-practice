import math
import sys
def input():return sys.stdin.readline().rstrip()
MAX=int(1e11)
N=int(input())
M=int(input())
res=0
res2=-1
def chk(num):
    if num==1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if not num%i:
            return False
    return True
for i in range(N,M+1):
    if chk(i):
        res+=i
        if res2==-1:
            res2=i
if res2==-1:
    print(res2)
else:
    print(res)
    print(res2)