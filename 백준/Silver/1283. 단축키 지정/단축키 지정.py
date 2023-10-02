import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
st=set()
a=[input() for _ in range(N)]
res_v=[-1 for _ in range(N)]
for i,cur in enumerate(a):
    s=cur
    f=0
    for cur2 in s:
        l=cur2.lower()
        if not l in st:
            f=1
            break
    if f:
        b=s.split()
        f=0
        idx=0
        for j in range(len(b)):
            c = str.lower(b[j][idx])
            if not c in st:
                st.add(c)
                pos=0
                for k in range(j):
                    pos+=len(b[k])+1
                res_v[i]=pos
                f=1
                break
        if not f:
            for j in range(len(s)):
                if s[j]==' ':continue
                ss=str.lower(s[j])
                if not ss in st:
                    st.add(ss)
                    res_v[i]=j
                    break
for i,cur in enumerate(a):
    if res_v[i]=='':continue
    for j in range(len(cur)):
        if j==res_v[i]:
            print('['+cur[j]+']',end='')
        else:
            print(cur[j],end='')
    print('')