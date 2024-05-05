from collections import *
def solution(spell, dic):
    answer = 0
    for cur in dic:
        c = Counter(cur)
        k = c.values()
        f = 1
        if len(k) != len(spell):
            continue
        for cur2 in spell:
            if c[cur2] != 1:
                f = 0
                break
        if f:
            return 1
    return 2