import math
def solution(n):
    answer = 0
    s=int(math.sqrt(n))
    if s*s==n:
        return pow(s+1,2)
    return -1