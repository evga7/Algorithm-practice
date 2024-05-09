def solution(data, ext, val_ext, sort_by):
    answer = []
    m={'code':0,'date':1,'maximum':2,'remain':3}
    idx=m[ext]
    for cur in data:
        if cur[idx]<val_ext:
            answer.append(cur)
    answer.sort(key=lambda x:x[m[sort_by]])
    return answer