import sys
def input():return sys.stdin.readline().rstrip()
s=input()
res=987654321
cmp=list(s)
cmp.sort()
for i in range(len(s)):
    ss=s[i:]+s[:i]
    cnt=0
    temp=list(ss)
    left=0
    right=len(ss)-1
    while cmp!=temp and left<right:
        while temp[left]!='b':
            left+=1
        while temp[right]!='a':
            right-=1
        temp[left],temp[right]=temp[right],temp[left]
        cnt+=1
    res=min(res,cnt)
    temp=list(ss)
    left=0
    right=len(ss)-1
    cnt=0
    while cmp!=temp and left<right:
        while temp[left]!='a':
            left+=1
        while temp[right]!='b':
            right-=1
        temp[left],temp[right]=temp[right],temp[left]
        cnt+=1
    res=min(res,cnt)

print(res)