def solution(t, p):
    answer = 0
    l=len(p)
    num=int(t[:l])
    idx=l
    p=int(p)
    ll=pow(10,l-1)
    while True:
        if num<=p:
            answer+=1
        if l==len(t):
            break
        num%=ll
        num=num*10+int(t[l])
        l+=1
    return answer