v=[]
def go(s,l,r,le):
    if len(str(s))>le:
        return
    if l<=s<=r:
        v.append(s)
    go(s*10,l,r,le)
    go(s*10+5,l,r,le)
def solution(l, r):
    answer = []
    go(5,l,r,len(str(r)))
    v.sort()
    if not v:
        v.append(-1)
    return v