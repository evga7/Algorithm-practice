import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[int(input()) for _ in range(N)]
a.sort(reverse=True)
cnt=0
res=0
for i,cur in enumerate(a):
    res+=cur
    cnt+=1
    if cnt==3:
        res-=cur
        cnt=0
print(res)