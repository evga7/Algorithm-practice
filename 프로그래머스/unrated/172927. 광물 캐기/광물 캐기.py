a=[[1,1,1],[5,1,1],[25,5,1]]
res=987654321
m=dict()
m["diamond"]=0
m["iron"]=1
m["stone"]=2
def go(idx,d,ir,s,minerals,p):
    if idx>=len(minerals) or (not d and not ir and not s):
        global res
        res=min(res,p)
        return
    dp=0
    ip=0
    sp=0
    for i in range(idx,min(idx+5,len(minerals))):
        dp+=a[0][m[minerals[i]]]
        ip+=a[1][m[minerals[i]]]
        sp+=a[2][m[minerals[i]]]
    if d:
        go(idx+5,d-1,ir,s,minerals,p+dp)
    if ir:
        go(idx+5,d,ir-1,s,minerals,p+ip)
    if sp:
        go(idx+5,d,ir,s-1,minerals,p+sp)
def solution(picks, minerals):
    global res
    go(0,picks[0],picks[1],picks[2],minerals,0)
    return res