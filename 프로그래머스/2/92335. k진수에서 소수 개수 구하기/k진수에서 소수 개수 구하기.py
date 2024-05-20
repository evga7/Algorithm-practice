import math
def chk(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if not num%i:
            return False
    return True
def conv(num,k):
    s=""
    while num:
        s+=str(num%k)
        num//=k
    return s[::-1]
def solution(n, k):
    answer = 0
    s=conv(n,k)
    t=""
    for cur in s:
        if cur!='0':
            t+=cur
        else:
            if t:
                tt=int(t)
                if tt>1 and chk(tt):
                    answer+=1
                t=""
    if t:
        tt=int(t)
        if tt>1 and chk(tt):
            answer+=1
    return answer