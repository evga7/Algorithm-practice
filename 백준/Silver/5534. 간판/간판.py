import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
s=input()
res=0
    
def chk(t):
    if not t.find(s):
        return True
    if len(t)<len(s):
        return False
    for i in range(len(t)):
        if t[i]==s[0]:
            for j in range(1,100):
                idx = 1
                for k in range(i+j,len(t),j):
                    if s[idx]!=t[k]:break
                    idx+=1
                    if idx==len(s):
                        return True
    return False
            
            
for i in range(N):
    t=input()
    if chk(t):
        res+=1
print(res)