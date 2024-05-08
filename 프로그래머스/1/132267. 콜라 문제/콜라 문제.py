def solution(a, b, n):
    answer = 0
    while n>=a:
        c=n//a
        answer+=c*b
        cc=n%a
        n=(c*b)+cc
    return answer