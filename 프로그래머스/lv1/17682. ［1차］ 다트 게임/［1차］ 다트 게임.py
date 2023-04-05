def c(s):
    if s=='D':
        return 2
    elif s=='T':
        return 3
    return 1
def solution(dartResult):
    answer = 0
    a=[]
    s=""
    for i,cur in enumerate(dartResult):
        s += cur
        if cur=='D' or cur=='S' or cur=='T':
            if i+1<len(dartResult):
                if dartResult[i + 1] == '*' or dartResult[i + 1] == '#':continue
            a.append(s)
            s=""
        elif cur=='*' or cur=='#':
            a.append(s)
            s=""
    if s:
        a.append(s)
    b=0
    aa=[]
    idx=0
    for cur in a:
        num=""
        for cc in cur:
            if not str.isdigit(cc):break
            num+=cc
        if len(num)>1:
            bonus=cur[2]
        else:
            bonus=cur[1]
        num=int(num)
        if cur[-1]=='#' or cur[-1]=='*':
            op=cur[2]
            num=pow(num,c(bonus))
            if op=='*':
                op=2
                if idx-1>=0:
                    aa[idx-1]*=2
            else:
                op=-1
            num*=op
            aa.append(num)
        else:
            aa.append(pow(num, c(bonus)))
        idx+=1

    return sum(aa)