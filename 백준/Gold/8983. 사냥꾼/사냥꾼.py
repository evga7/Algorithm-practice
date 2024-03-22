import sys
def input():
    return sys.stdin.readline().rstrip()
N,M,L=map(int,input().split())
a=list(map(int,input().split()))
b=[list(map(int,input().split())) for _ in range(M)]
a.sort()
res=0
for cur in b:
    S,E=cur[0],cur[1]
    Le=E-L+S
    Ri=L-E+S
    left=0
    right=N-1
    while left<=right:
        mid=left+right>>1
        if Le<=a[mid]<=Ri:
            res+=1
            break
        elif Le>a[mid]:
            left=mid+1
        elif Ri<a[mid]:
            right=mid-1
print(res)