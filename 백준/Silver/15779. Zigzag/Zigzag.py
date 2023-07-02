import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
arr=list(map(int,input().split()))
res=2
left=0
right=2
def chk(a,b,c):
    if a<=b<=c:
        return False
    if a>=b>=c:
        return False
    return True
while left<right and right<N:
    if chk(arr[right],arr[right-1],arr[right-2]):
        res = max(res, right - left+1)
        right+=1
    else:
        left+=1
        right+=1

print(res)