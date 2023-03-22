import math
def solution(arr):
    answer = 1
    for cur in arr:
        answer=answer*cur // math.gcd(cur,answer)
    return answer