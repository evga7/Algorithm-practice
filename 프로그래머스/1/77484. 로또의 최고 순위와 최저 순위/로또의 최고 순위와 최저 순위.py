from collections import *
s=[6,6,5,4,3,2,1]
    
def solution(lottos, win_nums):
    answer = []
    st=set(win_nums)
    c=Counter(lottos)
    r=len(st&c.keys())
    return [s[r+c[0]],s[r]]