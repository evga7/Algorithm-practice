import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
for i in range(N):
    res=0
    arr=list(map(int,input().split()))
    for j in range(1,len(arr)):
        cur=arr[j]
        cnt=0
        for k in range(j+1,len(arr)):
            if cur>arr[k]:
                cnt+=1
        res+=cnt
    print(i+1,res)