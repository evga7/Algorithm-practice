def solution(s):
    r1,r2=0,0
    while len(s)>0 and s!='1':
        r2+=s.count('0')
        r1+=1
        s=s.replace('0','')
        s=bin(len(s))[2:]
    
    return [r1,r2]