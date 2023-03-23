def solution(s):
    cnt=0
    z=0
    while s!='1':
        cnt+=1
        c=s.count('0')
        z+=c
        s=bin(len(s)-c)[2:]
    return [cnt,z]