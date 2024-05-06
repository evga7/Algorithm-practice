def solution(numbers, k):
    answer = 0
    l=len(numbers)
    k-=1
    return numbers[(2*k)%l]
