import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
arr=list(map(int,input().split()))
res1=0
res2=1
s=0
cnt=0
for i in range(M):
    s+=arr[i]
if s:
    res2=1
res1=max(res1,s)
left=0
right=M
while right<N:
    s-=arr[left]
    left+=1
    s+=arr[right]
    right+=1
    if s:
        if res1<=s:
            if res1==s:
                res2+=1
                continue
            res1=s
            res2=1
if not res1:
    print("SAD")
else:
    print(res1)
    print(res2)