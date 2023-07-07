import sys
def input(): return sys.stdin.readline().rstrip()
s=input()
st2=set()
v=[]
vi=[0 for _ in range(201)]
st=[]
for i in range(len(s)):
    if s[i]=='(':
        st.append(i)
    elif s[i]==')':
        v.append((st[-1],i))
        st.pop()
c=[0 for _ in range(201)]
def go(idx,cnt):
    if cnt:
        ss=""
        global s
        for i in range(len(s)):
            if c[i]:continue
            ss+=s[i]
        st2.add(ss)
    for i in range(idx,len(v)):
        if vi[i]:continue
        vi[i]=1
        start,end=v[i][0],v[i][1]
        c[start]=1
        c[end]=1
        go(i+1,cnt+1)
        vi[i]=0
        c[start]=0
        c[end]=0
go(0,0)
res_v=list(st2)
res_v.sort()
for cur in res_v:
    print(cur)