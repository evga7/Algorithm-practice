cnt=0
s=input()
l=len(s)
last=0
c=1
st=set()
v=[]
for i in range(1,51):
    if i==10:
        c+=1
    cnt+=c
    if cnt==l:
        last=i
        break
def go(idx):
    if idx==l:
        print(*v)
        exit(0)
    a=int(s[idx])
    if idx+1<l:
        b=s[idx]+s[idx+1]
        b=int(b)
        if 1<=b<=last and not b in st:
            st.add(b)
            v.append(b)
            go(idx + 2)
            st.remove(b)
            v.pop()
    if 1<=a<=last and not a in st:
        st.add(a)
        v.append(a)
        go(idx+1)
        v.pop()
        st.remove(a)

go(0)