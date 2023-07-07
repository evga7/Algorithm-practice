import sys
def input(): return sys.stdin.readline().rstrip()
s=input()
st=set()
def go(s,idx):
    cnt=1
    for i in range(idx+1,len(s)):
        if s[i]=='(':cnt+=1
        elif s[i]==')':
            cnt-=1
            if cnt==0:
                idx2=i
                break
    s2=""
    for i in range(len(s)):
        if i==idx or i==idx2:continue
        s2+=s[i]
    return s2
v=[]
v.append(s)
while True:
    v2=[]
    for cur in v:
        for i in range(len(cur)):
            if cur[i]=='(':
                c=go(cur,i)
                if not c in st:
                    v2.append(c)
                    st.add(c)
    if not v2:
        break
    v=v2[:]
res_v=list(st)
res_v.sort()
for cur in res_v:
    print(cur)