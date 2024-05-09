from collections import *
def solution(participant, completion):
    c,c2=Counter(participant),Counter(completion)
    return list((c-c2).keys())[0]