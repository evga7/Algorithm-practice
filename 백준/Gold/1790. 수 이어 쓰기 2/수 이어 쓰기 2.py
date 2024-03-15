import sys
def input(): return sys.stdin.readline().rstrip()
N,K=map(int,input().split())
res=0
num=10
cnt=1
for i in range(1,N+1):
    if i==num:
        cnt+=1
        num*=10
    if res+cnt>=K:
        ss=str(i)
        print(ss[K-res-1])   
        exit(0)
    res+=cnt
print(-1)