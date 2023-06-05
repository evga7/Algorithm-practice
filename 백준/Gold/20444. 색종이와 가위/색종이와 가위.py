import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
left=0
right=N//2
while left<=right:
    mid=left+right>>1
    s=(mid+1)*(N-mid+1)
    if s>=M:
        if s==M:
            print("YES")
            exit(0)
        right=mid-1
    else:
        left=mid+1
print("NO")