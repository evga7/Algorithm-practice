N,M=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
back=a[0]
res=1
for i in range(1,N):
    if a[i]-back<M:continue
    res+=1
    back=a[i]
print(res)