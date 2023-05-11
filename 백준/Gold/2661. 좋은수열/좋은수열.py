import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
f=0
def go(s,before):
    global f
    if f:
        return
    for i in range(2,len(s)//2+1):
        for j in range(len(s)-i):
            ss=s[j:j+i]
            ss2=s[j+i:j+i*2]
            if ss==ss2:
                return


    if len(s)==N:
        print(s)
        f=1
        return
    for i in range(1,4):
        if i==before:continue
        go(s+str(i),i)

go('1',1)