import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
M=int(input())
a=list(map(int,input().split()))
b=[]
a.sort()
for i in range(1,len(a)):
    b.append(a[i]-a[i-1])
b.sort(reverse=True)
print(sum(b[M-1:]))