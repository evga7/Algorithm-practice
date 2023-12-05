import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
s=input()
s=s.replace("pi"," ")
s=s.replace("ka"," ")
s=s.replace("chu"," ")
s=s.replace(" ","")
if s:
    print("NO")
else:
    print("YES")