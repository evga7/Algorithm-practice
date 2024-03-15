import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
res=0
if N<10:
    print(N)
    exit(0)
else:
    res=9
    num=100
    cnt=2
    for i in range(10,N+1):
        if i==num:
            cnt+=1
            num*=10
        res+=cnt
print(res)