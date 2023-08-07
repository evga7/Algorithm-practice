dx=[1,1,1,0,0,0,-1,-1,-1]
dy=[-1,0,1,-1,0,1,-1,0,1]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
import sys
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
robot=set()
x,y=0,0
for i in range(N):
    for j in range(M):
        if a[i][j]=='R':
            robot.add((i,j))
        elif a[i][j]=='I':
            x,y=i,j
op=list(map(int,input()))
def find_pos(n_x,n_y,rx,ry):
    cnt=987654321
    xx,yy=rx,ry
    for i in range(9):
        rn_x,rn_y=rx+dx[i],ry+dy[i]
        pos=abs(n_x-rn_x)+abs(n_y-rn_y)
        if pos<cnt:
            cnt=pos
            xx,yy=rn_x,rn_y
    return (xx,yy)
def print_map():
    for i in range(N):
        for j in range(M):
            if i == x and y == j:
                print('I', end='')
            elif (i, j) in robot:
                print('R', end='')
            else:
                print('.', end='')
        print('')
    print('')

def go():
    idx=0
    global robot,x,y
    while idx<len(op):
        x+=dx[op[idx]-1]
        y+=dy[op[idx]-1]
        visited=set()
        nxt_robot=set()
        for cur in robot:
            rx,ry=cur[0],cur[1]
            xx,yy=find_pos(x,y,rx,ry)
            if (xx,yy)==(x,y):
                print("kraj %s"%(idx+1))
                exit(0)
            if (xx,yy) in nxt_robot:
                visited.add((xx,yy))
            nxt_robot.add((xx,yy))
        for cur in visited:
            xx,yy=cur[0],cur[1]
            if (xx,yy) in nxt_robot:
                nxt_robot.remove((xx,yy))
        robot=nxt_robot
        idx+=1

go()
print_map()