import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
res1,res2,res3=0,0,0
def go(s,x,y):
    cur=a[x][y]
    f=1
    global res1,res2,res3
    for i in range(x,x+s):
        for j in range(y,y+s):
            if cur!=a[i][j]:
                f=0
                break
        if cur != a[i][j]:
            break
    if f:
        if cur==-1:
            res1+=1
        elif cur==0:
            res2+=1
        elif cur==1:
            res3+=1
    else:
        ss=s//3
        s2=ss*2
        go(ss,x,y)
        go(ss,x,y+ss)
        go(ss, x, y + s2)
        go(ss, x+ss, y)
        go(ss, x+ss,y+ss)
        go(ss,x+ss,y+s2)
        go(ss, x + s2, y)
        go(ss, x + s2, y + ss)
        go(ss,x+s2,y+s2)
        
        
go(N,0,0)
print(res1)
print(res2)
print(res3)

