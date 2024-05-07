def solution(s):
    l=len(s)
    return s[l//2] if l&1 else s[l//2-1:l//2+1]