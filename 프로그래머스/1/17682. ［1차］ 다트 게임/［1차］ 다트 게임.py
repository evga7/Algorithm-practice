def score(num,bonus,op):
    ss=num
    if bonus=='D':
        ss=pow(ss,2)
    elif bonus=='T':
        ss=pow(ss,3)
    if op=='#':
        ss*=-1
    return ss
        
    
    
def solution(dartResult):
    answer = 0
    tem=""
    l=len(dartResult)
    num=[]
    bonus=[]
    op=[]
    n=""
    for i,cur in enumerate(dartResult):
        if cur.isdigit():
            n+=cur
        elif cur.isalpha():
            num.append(int(n))
            n=""
            bonus.append(cur)
            if i+1<l and (dartResult[i+1]=='#' or dartResult[i+1]=='*'):
                op.append(dartResult[i+1])
            else:
                op.append('')
    a=[]
    for i in range(3):
        s=score(num[i],bonus[i],op[i])
        if op[i]=='*':
            s*=2
            if i-1>=0:
                a[i-1]*=2
        a.append(s)
    return sum(a)