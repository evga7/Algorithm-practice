import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
idx=0
s=sum(a)
if s>M:
    c=M//s
    M-=s*c
op=1
M+=1
while True:
    M-=a[idx]
    if M<=0:
        print(idx+1)
        exit(0)
    idx+=op
    if idx==N or idx==-1:
        op*=-1
        idx+=op