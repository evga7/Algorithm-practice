import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
J,S=N,N
a=list(map(int,input().split()))
j,s=0,0
for i in range(14):
    cur=a[i]
    if i-3>=0:
        if a[i-3]<a[i-2]<a[i-1]:
            if s:
                S+=s*cur
                s=0
        elif a[i-3]>a[i-2]>a[i-1]:
            cnt = S // cur
            s += cnt
            S -= cur * cnt
    if cur<=J:
        cnt=J//cur
        j+=cnt
        J-=cur*cnt
res1=j*a[-1]+J
res2=s*a[-1]+S
if res1>res2:
    print("BNP")
elif res1<res2:
    print("TIMING")
else:
    print("SAMESAME")