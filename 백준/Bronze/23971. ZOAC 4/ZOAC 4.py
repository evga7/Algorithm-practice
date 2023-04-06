import sys
def input():return sys.stdin.readline().rstrip()
N,M,n,m=map(int,input().split())
n+=1
m+=1
print(((N+(n-1))//n)*((M+(m-1))//m))
