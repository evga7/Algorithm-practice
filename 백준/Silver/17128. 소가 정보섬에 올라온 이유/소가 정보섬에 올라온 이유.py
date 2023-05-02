import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
left=0
right=4
s=1
for i in range(4):
    s*=a[i]
v=[]
while True:
    v.append(s)
    if left==N-1:
        break
    s/=a[left]
    left+=1
    s*=a[right]
    right+=1
    right%=N
res=int(sum(v))
for cur in b:
    idx=(cur-4+N)%N
    cnt=0
    for i in range(4):
        res-=v[idx]
        v[idx]*=-1
        res+=v[idx]
        idx+=1
        idx%=N
    print('%d'%res)