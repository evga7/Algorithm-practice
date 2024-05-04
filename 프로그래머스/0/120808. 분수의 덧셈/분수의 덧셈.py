import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    b=(numer1*denom2)+(numer2*denom1)
    a=denom1*denom2
    cd=math.gcd(a,b)
    answer.append(b//cd)
    answer.append(a//cd)
    return answer