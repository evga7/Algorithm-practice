import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
a=[]
for i in range(3):
    q,w,e=input().split()
    a.append((int(q),int(w),e))

v=[]
v.append(a[0][1]%100)
v.append(a[1][1]%100)
v.append(a[2][1]%100)
v.sort()
a.sort(reverse=True)
print('%d%d%d'%(v[0],v[1],v[2]))
print('%c%c%c'%(a[0][2][0],a[1][2][0],a[2][2][0]))