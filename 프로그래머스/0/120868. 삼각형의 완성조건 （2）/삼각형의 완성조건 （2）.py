def solution(sides):
    m,mi=max(sides),min(sides)
    answer=0
    answer+=m-(m-mi)
    answer+=sum(sides)-m-1
    return answer