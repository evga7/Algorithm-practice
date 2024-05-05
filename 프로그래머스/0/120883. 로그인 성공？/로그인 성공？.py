def solution(id_pw, db):
    answer = ''
    idt=set()
    pwt=set()
    st=set()
    i,p=id_pw[0],id_pw[1]
    for x,y in db:
        idt.add(x)
        pwt.add(y)
        st.add((x,y))
    if i in idt:
        if (i,p) in st:
            answer="login"
        else:
            answer="wrong pw"
    else:
        answer="fail"

    return answer