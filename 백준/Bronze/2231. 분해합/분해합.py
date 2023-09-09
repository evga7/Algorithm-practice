import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize

def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
N=int(input())
for i in range(1,N+1):
    temp=i
    s=0
    while temp:
        s+=temp%10
        temp//=10
    if i+s==N:
        print(i)
        exit(0)
print(0)