
def solution(quiz):
    answer = []
    for cur in quiz:
        q=cur[:cur.find('=')]
        a = cur[cur.find('=')+2:]
        if eval(q)==int(a):
            answer.append('O')
        else:
            answer.append('X')
    return answer