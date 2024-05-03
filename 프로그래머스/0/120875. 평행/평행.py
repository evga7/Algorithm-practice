def chk(a,b,dots):
    v=[]
    c,d=0,0
    for i in range(4):
        if not i==a and not i==b:
            if not c:
                c=i
            else:
                d=i
    x1,y1,x2,y2=dots[a][0],dots[a][1],dots[b][0],dots[b][1]
    x3,y3,x4,y4=dots[c][0],dots[c][1],dots[d][0],dots[d][1]
    q=(y1-y2)/(x1-x2)
    q2=(y3-y4)/(x3-x4)
    if q==q2:
        return True
    
        
def solution(dots):
    answer = 0
    for i in range(4):
        for j in range(i+1,4):
            if chk(i,j,dots):
                return 1
    return 0