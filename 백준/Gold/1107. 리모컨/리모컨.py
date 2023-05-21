import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
M=int(input())
c = [1 for _ in range(10)]
if M:
    a=list(map(int,input().split()))
    for cur in a:
        c[cur]=0
res=abs(N-100)
ss='100'
for i in range(0,1000000):
    s=str(i)
    f=1
    for cur in s:
        if not c[ord(cur)-ord('0')]:
            f=0
            break
    if f:
        res = min(res, len(s) + abs(N - i))


print(res)