def solution(s):
    l=len(s)
    if (l==4 or l==6) and s.isdecimal():
        return True
    return False