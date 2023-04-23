import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
res=int(1e20)
left,right=0,0
s=a[0]
while True:
    if s>=M:
        res = min(res, right - left+1)
        s -= a[left]
        left += 1
    else:
        right += 1
        if right==N:
            break
        s += a[right]

if res==int(1e20):
    res=0
print(res)