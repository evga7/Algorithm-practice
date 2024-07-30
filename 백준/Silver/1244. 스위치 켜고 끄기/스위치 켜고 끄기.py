import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=[0]+list(map(int,input().split()))
M=int(input())
for i in range(M):
    q,w=map(int,input().split())
    if q==1:
        for j in range(w,N+1,w):
            a[j]=1-a[j]
    else:
        a[w]=1-a[w]
        left=w
        right=w
        while left-1>0 and right+1<=N and a[left-1]==a[right+1]:
            left-=1
            right+=1
            a[left]=1-a[left]
            a[right]=1-a[right]
for i in range(1,N+1):
    print(a[i],end=' ')
    if not i%20:
        print('')
