import sys
def input():
    return sys.stdin.readline().rstrip()
res=0
A,B,C,X,Y=map(int,input().split())
res2=987654321
res=0
mm=0
mim=0
if X>Y:
    m=X
    mi=Y
    mm=A
    mim=B
else:
    m=Y
    mi=X
    mm=B
    mim=A
sub=m-mi
if C*2>=A+B:
    res=A*X+B*Y
else:
    res=(C*2*mi)+(mm*sub)
    res2=(C*2*m)
print(min(res,res2))
