import math
def solution(n):
    answer = []
    n2=n
    i=2
    while i<=n2:
        if not n%i:
            answer.append(i)
            while not n%i:
                n//=i
        else:
            i+=1
    return answer