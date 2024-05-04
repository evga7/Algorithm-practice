def solution(polynomial):
    answer = ''
    v=polynomial.split(' ')
    x=0
    num=0
    for cur in v:
        if cur=='+':continue
        idx=cur.find('x')
        if idx>=0:
            if len(cur)==1:
                x+=1
            else:
                x+=int(cur[:idx])
        else:
            num+=int(cur)
    if x:
        if x==1:
            answer='x'
        else:
            answer=str(x)+'x'
    if num:
        if answer:
            answer+=' + '+str(num)
        else:
            answer=str(num)
    return answer
print(solution("1 + x"))