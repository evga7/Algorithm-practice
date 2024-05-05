def solution(dots):
    answer = 0
    x_mx,x_mi=-257,256
    y_mx,y_mi=-257,256
    for x,y in dots:
        x_mx=max(x,x_mx)
        x_mi=min(x,x_mi)
        y_mx=max(y,y_mx)
        y_mi=min(y,y_mi)
    return (x_mx-x_mi)*(y_mx-y_mi)
    