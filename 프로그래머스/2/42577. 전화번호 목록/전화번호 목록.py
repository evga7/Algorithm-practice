def solution(phone_book):
    phone_book.sort(key=lambda x:len(x))
    st=set()
    l=len(phone_book)
    st.add(phone_book[0])
    for i in range(1,l):
        cur=phone_book[i]
        s=""
        for c in cur:
            s+=c
            if s in st:
                return False
        st.add(cur)
    return True