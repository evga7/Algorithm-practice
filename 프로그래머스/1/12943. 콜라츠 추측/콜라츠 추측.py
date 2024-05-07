def solution(num):
    answer = 0
    c=0
    while c<500 and num>1:
        c+=1
        if not num&1:
            num//=2
        else:
            num=(num*3)+1
    return c if c<500 else -1