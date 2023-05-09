import sys
def input():return sys.stdin.readline().rstrip()
N=input()
res2=0
res1=999999999
def go(s,cnt):
    for cur in s:
        if int(cur)&1:
            cnt+=1
    if len(s)==1:
        global res1,res2
        res2=max(res2,cnt)
        res1=min(res1,cnt)
        return
    if len(s)==2:
        go(str(int(s[0])+int(s[1])),cnt)
    else:
        for i in range(len(s)):
            for j in range(i+1,len(s)-1):
                nxt=int(s[:i+1])+int(s[i+1:j+1])+int(s[j+1:])
                go(str(nxt),cnt)
go(N,0)
print('%d %d'%(res1,res2))