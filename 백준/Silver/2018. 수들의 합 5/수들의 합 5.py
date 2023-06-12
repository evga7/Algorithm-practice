import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
left=1
right=1
res=0
s=0
while left<=N:
    if s>=N:
        if s==N:
            res+=1
        s-=left
        left+=1
    else:
        s+=right
        right+=1
print(res)