def solution(x):
    answer = False
    n=x
    s=0
    while x:
        s+=x%10
        x//=10
    if not n%s:
        answer=True
    return answer