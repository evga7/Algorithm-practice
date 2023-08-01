import sys
from collections import *
dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
def is_inside(x,y,N,M):
    return 0<x<=N and 0<y<=M
def input():return sys.stdin.readline().rstrip()

chk=["clap","stomp","clap"]
def c1():
    f=0
    for i ,cur in enumerate(s):
        if cur=='dip':
            q1,q2,q3='','',''
            if i-1>=0:
                q1=s[i-1]
            if i-2>=0:
                q2=s[i-2]
            if i+1<len(s):
                q3=s[i+1]
            if q1=="jiggle" or q2=="jiggle" or q3=="twirl":continue
            s[i]="DIP"
            f=1
    return f
def c2():
    f=0
    s1=s[len(s)-3:]
    if s1!=chk:
        f=2
    return f
def c3():
    f=0
    if "twirl" in st:
        if not "hop" in st:
            f=3
    return f
def c4():
    f=0
    if s and s[0]=="jiggle":
        f=4
    return f
def c5():
    f=0
    if not "dip" in st:
        f=5
    return f
while True:
    s=input().split()
    st=set(s)
    if not s:
        break
    e = []
    f=c1()
    if f:
        e.append(f)
    f=c2()
    if f:
        e.append(f)
    f=c3()
    if f:
        e.append(f)
    f=c4()
    if f:
        e.append(f)
    f=c5()
    if f:
        e.append(f)
    if not e:
        print("form ok: ",end='')
    else:
        ss=''
        for i,cur in enumerate(e):
            if i == len(e) - 1:
                if len(e)>1:
                    ss+='and'+' '+str(cur)
                else:
                    ss+=str(cur)
            elif i+1==len(e)-1:
                ss+=str(cur)+' '
            else:
                ss+=str(cur)+','+' '
        if len(e)==1:
            print("form error %s: "%ss,end='')
        else:
            print("form errors %s: "%ss,end='')
    print(*s)