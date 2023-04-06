import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
n=0
res=1
n=1
while True:
    if n>=N:break
    n+=6*res
    res+=1
print(res)