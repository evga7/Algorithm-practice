def solution(sizes):
    answer = 0
    xx,yy=0,0
    for x,y in sizes:
        if x<y:
            x,y=y,x
        xx=max(xx,x)
        yy=max(yy,y)
    return xx*yy