N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
p=[[987654321 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        p[i+1][j+1]=a[i][j]
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if p[i][k]+p[k][j]<p[i][j]:
                p[i][j]=p[i][k]+p[k][j]
for i in range(M):
    a,b,c=map(int,input().split())
    if p[a][b]<=c:
        print("Enjoy other party")
    else:
        print("Stay here")