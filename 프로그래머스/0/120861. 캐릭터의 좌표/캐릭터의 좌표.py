def solution(keyinput, board):
    answer = []
    m={'left':(0,-1),'right':(0,1),'up':(1,1),'down':(1,-1)}
    p=[0,0]
    x_max=board[0]//2
    x_min=-x_max
    y_max=board[1]//2
    y_min=-y_max
    for cur in keyinput:
        pos=m[cur][0]
        op=m[cur][1]
        p[pos]+=op
        if pos==0:
            p[pos]=min(x_max,p[pos])
            p[pos]=max(x_min,p[pos])
        else:
            p[pos]=min(y_max,p[pos])
            p[pos]=max(y_min,p[pos])
    return p