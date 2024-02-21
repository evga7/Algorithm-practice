import sys
def input():return sys.stdin.readline().rstrip()
a=[int(input()) for _ in range(9)]
a.sort()
s=sum(a)
def p(x,y):
    for i in range(9):
        if i==x or i==y:continue
        print(a[i])
    exit(0)
for i in range(9):
    for j in range(i+1,9):
        if (s-a[i]-a[j])==100:
            p(i,j)
        
        
