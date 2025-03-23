-- 코드를 입력하세요
SELECT b.USER_ID,b.NICKNAME,concat(b.CITY," ",b.STREET_ADDRESS1," ",b.STREET_ADDRESS2) 전체주소,
concat(left(TLNO,3),"-",substring(tlno,4,4),"-",right(tlno,4)) 전화번호 from USED_GOODS_BOARD a join USED_GOODS_USER b on a.WRITER_ID=b.USER_ID
where a.WRITER_ID in (select WRITER_ID from USED_GOODS_BOARD group by WRITER_ID having count(*)>=3 )
group by a.writer_id
order by USER_ID desc
