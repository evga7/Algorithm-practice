import re
def solution(dartResult):
    aa=[]
    a=re.compile('(\d+)([SDT])([#*]?)')
    v=a.findall(dartResult)
    bo={'S':1,'D':2,'T':3}
    for cur in v:
        num=int(cur[0])
        bonus=cur[1]
        op=cur[2]
        c=num**bo[bonus]
        if op=='*':
            if aa:
                aa[-1]*=2
            c*=2
        elif op=='#':
            c*=-1
        aa.append(c)
    return sum(aa)