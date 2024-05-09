def solution(wallpaper):
    answer = []
    n,m=len(wallpaper),len(wallpaper[0])
    x,y,x2,y2=51,51,-1,-1
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j]=='#':
                x,y=min(x,i),min(y,j)
                x2,y2=max(x2,i),max(y2,j)
    return [x,y,x2+1,y2+1]