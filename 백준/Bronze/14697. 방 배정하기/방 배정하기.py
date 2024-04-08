*a,d=list(map(int,input().split()))
idx=2
while d:
    if a[idx]>d:
        idx-=1
        if idx==-1:
            break
        continue
    c=d//a[idx]
    d-=a[idx]*c
if d:
    print(0)
else:
    print(1)