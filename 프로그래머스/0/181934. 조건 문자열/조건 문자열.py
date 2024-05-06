def f(a,b,c,d):
    if c=='<':
        if d=='=':
            if a<=b:
                return 1
        else:
            if a<b:
                return 1
    elif c=='>':
        if d=='=':
            if a>=b:
                return 1
        else:
            if a>b:
                return 1
    return 0
def solution(ineq, eq, n, m):
    return f(n,m,ineq,eq)