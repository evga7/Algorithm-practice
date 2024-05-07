def solution(numbers):
    st=set(numbers)
    answer=0
    for i in range(1,10):
        if not i in st:
            answer+=i
    return answer