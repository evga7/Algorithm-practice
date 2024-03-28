import sys
def input():
    return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
st=set()
v=[]
for cur in a:
    st.add(cur)
def go(idx,cur):
    if idx==N:
        print(*v)
        exit(0)
        return
    nxt=cur//3
    if not cur%3 and nxt in st:
        v.append(nxt)
        go(idx+1,nxt)
        v.pop()
    if cur*2 in st:
        v.append(cur*2)
        go(idx+1,cur*2)
        v.pop()
for cur in a:
    v.append(cur)
    go(1,cur)
    v.pop()