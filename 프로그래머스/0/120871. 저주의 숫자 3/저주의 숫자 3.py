def solution(n):
    answer = 0
    for i in range(1,n+1):
        answer+=1
        while str(answer).find('3')>=0 or not answer%3:
            answer+=1
    return answer