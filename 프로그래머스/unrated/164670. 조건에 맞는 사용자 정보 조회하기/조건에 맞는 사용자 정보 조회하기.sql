-- 코드를 입력하세요
SELECT b.USER_ID,b.NICKNAME	
,concat(b.CITY,' ',b.STREET_ADDRESS1,' ',b.STREET_ADDRESS2) 전체주소,
concat(left(tlno,3),'-',mid(tlno,4,4),'-',right(tlno,4)) 전화번호 from USED_GOODS_BOARD a join USED_GOODS_USER b on a.WRITER_ID=b.USER_ID
group by b.user_id
having count(a.WRITER_ID)>=3
order by b.user_id desc