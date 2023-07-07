import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
M=N
res=0
while N!=M or not res:
    temp=M
    temp=((temp%10)+(temp//10))%10
    M=(M%10)*10+temp
    res+=1
print(res)