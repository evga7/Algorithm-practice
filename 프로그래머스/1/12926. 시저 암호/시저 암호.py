def solution(s, n):
    answer = ''
    for cur in s:
        if cur.isalpha():
            c=ord(cur)+n
            if cur.isupper():
                c%=91
                if c<65:
                    c+=65
            else:
                c%=123
                if c<97:
                    c+=97
            answer+=chr(c)
        else:
            answer+=cur
    return answer