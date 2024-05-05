import math
def solution(a, b):
    answer = 0
    b=b/math.gcd(b,a)
    while b:
        if not b%5:
            b//=5
        elif not b%2:
            b//=2
        else:
            break
    if b==1:
        return 1
    return 2