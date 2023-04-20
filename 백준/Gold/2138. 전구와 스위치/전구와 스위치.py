import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
s=list(map(int,input()))
s2=list(map(int,input()))
res=987654321
def go(s1,b):
    cnt=0
    a=s1[:]
    for i in range(1,len(a)):
        if a[i-1]==b[i-1]:continue
        cnt+=1
        for j in range(i-1,min(i + 2, len(a))):
            a[j] ^= 1
    if a==b:
        return cnt
    else:
        return 987654321
res=min(res,go(s,s2))
s[0]^=1
s[1]^=1
res=min(res,go(s,s2)+1)
if res==987654321:
    res=-1
print(res)