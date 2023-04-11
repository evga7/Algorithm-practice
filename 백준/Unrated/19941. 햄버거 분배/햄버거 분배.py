import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
arr=list(input())
res=0
c=[0 for _ in range(N)]
for i in range(N):
    if arr[i]=='P':
        for j in range(max(0,i-M),min(i+M+1,N)):
            if not c[j] and arr[j]=='H':
                c[j]=1
                res+=1
                break
print(res)