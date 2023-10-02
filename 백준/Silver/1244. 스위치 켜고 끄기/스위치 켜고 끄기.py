import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
arr=list(map(int,input().split()))
M=int(input())
for i in range(M):
    a,b=map(int,input().split())
    if a==1:
        for j in range(b-1,N,b):
            arr[j]^=1
    else:
        b-=1
        left=b
        right=b
        while 0<=left-1 and right+1<N and arr[left-1]==arr[right+1]:
            left-=1
            right+=1
        for j in range(left,right+1):
            arr[j]^=1
for i in range(1,N+1):
    print(arr[i-1],end=' ')
    if not i%20:
        print('')