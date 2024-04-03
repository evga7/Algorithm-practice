N = int(input())
a=[float(input()) for _ in range(N)]
res=0
s=1
for cur in a:
    s*=cur
    s=max(s,cur)
    res=max(res,s)
print('%.3f'%res)