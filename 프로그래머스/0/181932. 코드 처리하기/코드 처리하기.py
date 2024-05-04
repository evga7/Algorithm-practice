def solution(code):
    answer = ''
    mode=0
    for i,cur in enumerate(code):
        if not mode:
            if cur!='1':
                if not i&1:
                    answer+=cur
            else:
                mode=1
        else:
            if cur!='1':
                if i&1:
                    answer+=cur
            else:
                mode=0
    if not answer:
        answer='EMPTY'
    return answer