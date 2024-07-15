import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
l=0
def go(s,cnt):
    if cnt==l:
        res_st.add(s)
        return
    if s in st:
        return
    st.add(s)
    for i in range(26):
        if a[i]:
            a[i]-=1
            go(s+chr(97+i),cnt+1)
            a[i]+=1

while N:
    N-=1
    s=input()
    a=[0 for _ in range(26)]
    l=len(s)
    st = set()
    res_st = set()
    for cur in s:
        a[ord(cur)-97]+=1
    go("",0)
    for cur in sorted(list(res_st)):
        print(cur)