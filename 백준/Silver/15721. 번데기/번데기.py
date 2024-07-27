import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N=int(input())
T=int(input())
M=int(input())
def go(num,pos,cnt):
    a=[0,1,0,1]
    for i in range(num+1):
        a.append(0)
    for i in range(num+1):
        a.append(1)
    for cur in a:
        if cur==M:
            cnt+=1
            if cnt==T:
                print(pos)
                exit(0)
        pos+=1
        pos%=N
    return (pos,cnt)
cnt=0
pos=0
num=0
while True:
    num+=1
    pos,cnt=go(num,pos,cnt)