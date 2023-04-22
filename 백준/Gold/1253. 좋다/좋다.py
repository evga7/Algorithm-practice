import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
arr=list(map(int,input().split()))

res=0
arr.sort()
for i,cur in enumerate(arr):
    a=arr[:i]+arr[i+1:]
    left,right=0,N-2
    while left<right:
        s=a[left]+a[right]
        if s>=cur:
            if s==cur:
                res+=1
                break
            right-=1
        else:
            left+=1
print(res)
