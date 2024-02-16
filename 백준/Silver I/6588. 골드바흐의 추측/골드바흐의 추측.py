import sys
import math
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
p=[0 for _ in range(1000001)]
def c():
    for i in range(2,int(math.sqrt(1000001))+1):
        if p[i]:continue
        for j in range(i+i,1000001,i):
            p[j]=1
c()
p[1]=1
st=set()
v=[]
for i in range(2,1000001):
    if not p[i]:
        st.add(i)
        v.append(i)
while True:
    N=int(input())
    if not N:
        break
    f=0
    for cur in v:
        sub=N-cur
        if N-cur in st:
            if cur>sub:
                cur,sub=sub,cur
            print(str(N)+' = '+str(cur)+' + '+str(sub))
            f=1
            break
    if not f:
        print("Goldbach's conjecture is wrong.")