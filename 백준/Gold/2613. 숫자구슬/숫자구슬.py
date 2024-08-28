import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N,M=map(int,input().split())
a=list(map(int,input().split()))
s=sum(a)
left=max(a)
right=s
mx,mi=0,987654321
mmx,mmi=0,987654321
while left<=right:
    mid =left+right>>1
    cnt=1
    s=0
    for cur in a:
        s+=cur
        if s>mid:
            s=cur
            cnt+=1
    if cnt<=M:
        right=mid-1
    else:
        left=mid+1
v=[]
res=0
back=0
s=0
print(left)
cnt=0
for i in range(N):
    s+=a[i]
    if s>left:
        v.append(cnt)
        cnt=0
        s=a[i]
        M-=1
    cnt+=1
    if N-i==M:
        break
while M:
    v.append(cnt)
    cnt=1
    M-=1
print(*v)