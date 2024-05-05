str = input()
for cur in str:
    if cur.isupper():
        print(cur.lower(),end='')
    else:
        print(cur.upper(),end='')
