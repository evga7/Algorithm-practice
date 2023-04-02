d=[set() for _ in range(9)]
def go(x,cnt):
    d[cnt].add(x)
    for i in range(1,cnt):
        for j in d[i]:
            for k in d[cnt-i]:
                d[cnt].add(j+k)
                d[cnt].add(j-k)
                d[cnt].add(j*k)
                if k:
                    d[cnt].add(j//k)

def solution(N, number):
    for i in range(1,9):
        a=int(str(N)*i)
        go(a,i)
        if number in d[i]:
            return i
    return -1