import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
def chk(a1,a2,a3,a4):
    temp=[]
    temp.append(a1)
    temp.append(a2)
    temp.append(a3)
    temp.append(a4)
    temp.sort(reverse=True)
    return temp[1]
def go(ar,s):
    if len(ar)==1:
        print(ar[0][0])
        return
    ar2=[]
    for i in range(0,s-1,2):
        temp=[]
        for j in range(0,s-1,2):
            temp.append(chk(ar[i][j],ar[i][j+1],ar[i+1][j],ar[i+1][j+1]))
        ar2.append(temp)
    go(ar2,s//2)

go(a,N)