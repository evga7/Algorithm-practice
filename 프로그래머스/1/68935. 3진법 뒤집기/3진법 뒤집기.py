def c(n):
    s=""
    while n:
        a=n%3
        s+=str(a)
        n//=3
    return s
def c2(n):
    s=1
    n2=0
    while n:
        if n%10:
            n2+=n%10*s
        s*=3
        n//=10
    return n2
        
def solution(n):
    answer = 0
    return c2(int(c(n)))