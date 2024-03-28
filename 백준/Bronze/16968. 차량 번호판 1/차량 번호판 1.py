s=input()
num=1
res=1
back='cc'
for i,cur in enumerate(s):
    if cur=='c':
        num=26
    else:
        num=10
    if cur==back:
        num-=1
    res*=num
        
    back=cur
print(res)