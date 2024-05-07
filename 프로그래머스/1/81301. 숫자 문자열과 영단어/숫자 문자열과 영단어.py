def solution(s):
    answer = 0
    v=[ "zero","one","two","three","four","five","six","seven","eight","nine"]
    for i,cur in enumerate(v):
        s=s.replace(cur,str(i)+' ')
    s=s.replace(' ','')
    return int(s)