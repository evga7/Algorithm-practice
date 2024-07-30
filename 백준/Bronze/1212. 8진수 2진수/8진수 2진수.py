import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N=input()

def go():
    if N == '0':
        print(0)
        return
    a=[]
    for cur in N:
        num=int(cur)
        a.append(str(num//4))
        a.append(str(num % 4 // 2))
        a.append(str(num % 4 % 2))
    f=0
    for i,cur in enumerate(a):
        if cur!='0':
            f=1
        if f:
            print(cur,end='')
go()