def solution(new_id):
    answer = ''
    new_id=new_id.lower()
    temp=""
    for cur in new_id:
        if cur.isalpha() or cur.isdigit() or cur=='-' or cur=='_' or cur=='.':
            temp+=cur
    new_id=temp
    temp=""
    for i,cur in enumerate(new_id):
        if cur=='.' and i-1>=0 and new_id[i-1]=='.':continue
        temp+=cur
    new_id=temp
    while new_id and new_id[0]=='.':
        new_id=new_id[1:]
    while new_id and new_id[-1]=='.':
        new_id=new_id[:-1]
    if not new_id:
        new_id="a"
    if len(new_id)>=16:
        new_id=new_id[:15]
    while new_id and new_id[-1]=='.':
        new_id=new_id[:-1]
    if len(new_id)<=2:
        new_id+=new_id[-1]*(3-len(new_id))
    return new_id
