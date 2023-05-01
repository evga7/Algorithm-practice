import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
T=int(input())
a=[list(map(int,input().split())) for _ in range(T)]
b=[]
for i,cur in enumerate(a):
    b.append((cur[0],cur[1],i))
    b.append((cur[1], cur[0],i))
res=0
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i][2]==b[j][2]:continue
        x1,y1,x2,y2=b[i][0],b[i][1],b[j][0],b[j][1]
        if ((x1+x2)<=N and max(y1,y2)<=M) or (y1+y2<=M and max(x1,x2)<=N):
            res=max(res,(x2*y2)+(x1*y1))
print(res)