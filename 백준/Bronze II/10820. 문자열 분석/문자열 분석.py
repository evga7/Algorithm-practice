import sys
INF = sys.maxsize
def input():
    return sys.stdin.readline().rstrip()
while True:
    s=sys.stdin.readline().rstrip('\n')
    if not s:
        break
    c1,c2,c3,c4=0,0,0,0
    for cur in s:
        if cur.islower():
            c1+=1
        elif cur.isupper():
            c2+=1
        elif cur.isdigit():
            c3+=1
        else:
            c4+=1
    print(c1,c2,c3,c4,end=' ')
    print('')