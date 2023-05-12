import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
a.sort()
res=0
for i in range(N-1):
    left=i+1
    right=N-1
    cur=a[i]
    while left<=right:
        mid=left+right>>1
        if a[mid]*0.9<=cur and cur<=a[mid]:
            left=mid+1
        else:
            right=mid-1
    res+=right-i
print(res)