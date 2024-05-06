def f(b):
    s=1
    for i in range(1,b+1):
       s*=i
    return s
    
def solution(balls, share):
    b,s=balls,share
    return f(b)//(f(b-s)*f(s))