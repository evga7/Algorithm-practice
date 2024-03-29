N,M=map(int,input().split())
a=list(map(int,input().split()))
s=[0 for _ in range(N+1)]
for i in range(1,N+1):
    s[i]=s[i-1]+a[i-1]
res=-987654321
for i in range(M,N+1):
    res=max(res,s[i]-s[i-M])
print(res)