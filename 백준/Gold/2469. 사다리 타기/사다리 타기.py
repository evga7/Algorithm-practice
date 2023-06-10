import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
K=int(input())
s=list(input())
a=[list(input()) for _ in range(K)]
idx=0
for i in range(N):
    if a[i][0]=='?':
        idx=i
        break
s1=[]
def go2():
    global s1,s
    for i in range(N):
        s1+=chr(ord('A')+i)
    for i in range(K):
        if a[i][0]=='?':
            break
        for j in range(N-1):
            if a[i][j]=='-':
                s1[j],s1[j+1]=s1[j+1],s1[j]
    a.reverse()
    for i in range(K):
        if a[i][0]=='?':
            break
        for j in range(N-1):
            if a[i][j]=='-':
                s[j],s[j+1]=s[j+1],s[j]
go2()
res=''
for i in range(len(s1)-1):
    if s1[i]==s[i]:
        res+='*'
    else:
        if s1[i]==s[i+1]:
            res+='-'
        elif i-1>=0 and s1[i]==s[i-1]:
            res+='*'
        else:
            print('x' * (N - 1))
            exit(0)
print(res)