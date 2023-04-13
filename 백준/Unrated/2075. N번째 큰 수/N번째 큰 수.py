import sys
import heapq
def input():return sys.stdin.readline().rstrip()
N=int(input())
q=[]
cnt=0
for i in range(N):
    a=list(map(int,input().split()))
    for cur in a:
        heapq.heappush(q,cur)
        if cnt>=N*N-N:break
        if len(q)>N:
            heapq.heappop(q)
            cnt+=1
    if cnt >= N * N - N: break

print(q[0])