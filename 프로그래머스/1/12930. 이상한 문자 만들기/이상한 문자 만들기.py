def solution(s):
    answer = ''
    c=0
    for i,cur in enumerate(s):
        if cur==' ':
            c=0
            answer+=' '
            continue
        if not c&1:
            answer+=cur.upper()
        else:
            answer+=cur.lower()
        c+=1
    return answer