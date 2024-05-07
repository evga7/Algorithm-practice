def solution(n):
    s=2
    while True:
        if n%s==1:
            return s
        s+=1