import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
left=1
right=2
f=0
while right<=100000:
    s=right**2-left**2
    if s>=N:
        if s==N:
            print(right)
            f=1
        left+=1
    else:
        right+=1
if not f:
    print(-1)