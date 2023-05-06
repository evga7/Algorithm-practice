N=int(input())
a=list(map(int,input().split()))
X=int(input())
a.sort()
left,right=0,N-1
res=0
while left<right:
    s=a[left]+a[right]
    if s>=X:
        if s==X:
            res+=1
        right-=1
    else:
        left+=1
print(res)