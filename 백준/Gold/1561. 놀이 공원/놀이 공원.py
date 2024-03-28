N,M=map(int,input().split())
a=list(map(int,input().split()))
if N<=M:
    print(N)
    exit(0)
left=0
right=int(2e15)
N-=M
while left<=right:
    mid=left+right>>1
    cnt=0
    for cur in a:
        cnt+=mid//cur
    if cnt>=N:
        right=mid-1
    else:
        left=mid+1

for cur in a:
    N-=right//cur
for i,cur in enumerate(a):
    if not (right+1)%cur:
        N-=1
    if not N:
        res=i+1
        break
print(res)