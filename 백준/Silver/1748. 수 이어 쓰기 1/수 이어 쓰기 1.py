import sys
def input():return sys.stdin.readline().rstrip() 
N=int(input())
res=9
cnt=0
cnt2=100
l=2
if N<10:
    print(N)
    exit(0)
for i in range(10,N+1):
    cnt+=1
    res+=l
    if cnt==int(cnt2*0.9):
        l+=1
        cnt2*=10
        cnt=0
print(res)