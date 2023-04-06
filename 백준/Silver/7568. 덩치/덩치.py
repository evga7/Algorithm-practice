import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
for i in range(len(arr)):
    res=1
    a,b=arr[i][0],arr[i][1]
    for j in range(len(arr)):
        if a<arr[j][0] and b<arr[j][1]:
            res+=1
    print(res,end=' ')