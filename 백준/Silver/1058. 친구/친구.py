import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[list(input()) for _ in range(N)]
m=0
for i in range(N):
    c=0
    for j in range(N):
        if a[i][j]=='Y':
            c+=1
            continue
        for k in range(N):
            if i==j:continue
            if a[k][i]=='Y' and a[k][j]=='Y':
                c+=1
                break
    m=max(m,c)
print(m)