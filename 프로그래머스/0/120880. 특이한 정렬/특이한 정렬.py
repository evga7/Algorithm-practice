def solution(numlist, n):
    answer = []
    a = numlist
    idx = 0
    l = len(a)
    s = 99898989898989
    v = []
    for i in range(l):
        ss = abs(n - a[i])
        if ss < s:
            s = ss
            idx = i
    answer.append(a[idx])
    for i, cur in enumerate(a):
        if a[idx] == cur: continue
        ss = abs(n - cur)
        v.append((ss, cur))
    v.sort(key=lambda x: (x[0],-x[1]))
    for x, y in v:
        answer.append(y)

    return answer