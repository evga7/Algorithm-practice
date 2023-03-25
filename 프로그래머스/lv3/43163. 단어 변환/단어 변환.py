res=987654321
v=[0 for _ in range(51)]
def chk(s1,s2):
    c=0
    if len(s1)!=len(s2):
        return False
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            c+=1
    if c>1:
        return False
    return True
def go(s,t,cnt,w):
    global res
    if s==t:
        res=min(res,cnt)
        return
    for i in range(len(w)):
        if not v[i] and chk(s,w[i]):
            v[i]=1
            go(w[i],t,cnt+1,w)
            v[i]=0

def solution(begin, target, words):
    answer = 0
    global res
    if not target in words:
        return 0
    go(begin,target,0,words)
    return res