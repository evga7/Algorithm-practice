import sys
import heapq
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
M=int(input())
b=list(map(int,input().split()))
b.sort(reverse=True)
q=[-cur for cur in a]
heapq.heapify(q)
if -q[0]<b[0]:
    print(-1)
    exit(0)
res=0
cnt=0
chk=[0 for _ in range(M)]
while cnt<M:
    temp=q[:]
    while temp:
        idx=0
        while temp and idx+1<M and (-temp[0]<b[idx] or chk[idx]):
            idx+=1
        if not chk[idx] and -temp[0]>=b[idx]:
            chk[idx] = 1
            cnt += 1
        heapq.heappop(temp)
    res+=1
print(res)