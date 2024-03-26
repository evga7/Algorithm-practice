N,K,P,X=map(int,input().split())
p=[63,6,91,79,102,109,125,7,127,111]
def chk(a,b):
    al=len(a)
    bl=len(b)
    if len(a)<len(b):
        a=(bl-al)*'0'+a
    elif len(a)>len(b):
        b = (al- bl) * '0' + b
    cnt=0
    l=max(al,bl)
    for i in range(l):
        if b[i]!=a[i]:
            bi=int(b[i])
            ai=int(a[i])
            for j in range(7):
                if (p[bi] & 1<<j)^(p[ai] & 1<<j):
                    cnt+=1
                if cnt>P:
                    return cnt
    return cnt
                
res=0
for i in range(1,N+1):
    s=chk(str(X),str(i))
    if 1<=s<=P:
        res+=1
    
print(res)
