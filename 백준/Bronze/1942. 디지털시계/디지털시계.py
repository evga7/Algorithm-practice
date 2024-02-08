import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
def c(h,m,s):
    return (h*3600) + (m*60)+s
def c2(h,m,s):
    if s==60:
        s=0
        m+=1
    if m==60:
        m=0
        h+=1
    if h==24:
        h=0
    return (h,m,s)
def c3(h,m,s):
    tt=(h*10000)+(m*100)+s
    if tt%3==0:
        return True
    return False
for i in range(3):
    res=0
    s1,s2=input().split()
    h1,m1,s1=int(s1[:2]),int(s1[3:5]),int(s1[6:8])
    h2,m2,s2=int(s2[:2]),int(s2[3:5]),int(s2[6:8])
    t1=c(h1,m1,s1)
    t2=c(h2,m2,s2)
    while True:
        if c3(h1,m1,s1):
            res+=1
        if t1==t2:
            break
        s1+=1
        h1,m1,s1=c2(h1,m1,s1)
        t1=c(h1,m1,s1)
    print(res)