import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
#map(int,input().split())
INF=sys.maxsize
s1=input()
s2=input()
h1=int(s1[:2])
h2=int(s2[:2])
m1=int(s1[3:5])
m2=int(s2[3:5])
ss1=int(s1[6:8])
ss2=int(s2[6:8])
T1=int((h1*3600)+(m1*60)+ss1)
T2=int((h2*3600)+(m2*60)+ss2)
if T1>=T2:
    T2+=86400
resT=abs(T1-T2)
print("%02d:%02d:%02d" % (resT//3600, (resT//60)%60, resT%60))