import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
for num in range(6,101):
    for i in range(2,101):
        for j in range(i+1,101):
            for k in range(j+1,101):
                if (pow(i,3)+pow(j,3)+pow(k,3))==pow(num,3):
                    print("Cube = %d, Triple = (%d,%d,%d)"% (num,i,j,k))