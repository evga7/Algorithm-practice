def solution(n):
    answer = 0
    a=bin(n)[2:].count('1')
    m=n+1
    while True:
        if a==bin(m)[2:].count('1'):
            return m
        m+=1
    return answer