import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
s=input()
ss=[]
l=len(s)
visited=[0 for _ in range(11)]
res=0
st=set()
def go2(ss):
    for i in range(1, l):
        if ss[i] == ss[i - 1]:
            return False
    return True
def go(cnt,sss):
    if cnt==l:
        global res
        if go2(sss):
            st.add(sss)
        return
    for i in range(l):
        if visited[i]:continue
        visited[i]=1
        go(cnt+1,sss+s[i])
        visited[i]=0
go(0,"")
print(len(st))