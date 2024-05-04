def cal(n):
    return n*(n+1)//2
def solution(num, total):
    answer = []
    right=1000
    while True:
        if cal(right)-cal(right-num)==total:
            for i in range(right-num+1,right+1):
                answer.append(i)
            return answer
        right-=1
    return answer