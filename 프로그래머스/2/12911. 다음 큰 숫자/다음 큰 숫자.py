def solution(n):
    answer = n+1
    c=bin(n)[2:].count('1')
    while True:
        if bin(answer)[2:].count('1')==c:
            break
        answer+=1
    return answer