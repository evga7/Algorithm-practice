-- 코드를 입력하세요
SELECT USER_ID,NICKNAME
,concat(b.city,' ',b.STREET_ADDRESS1,' ',b.STREET_ADDRESS2) AS 전체주소
,concat(left(b.TLNO,3),'-',mid(b.TLNO,4,4),'-',right(b.TLNO,4)) AS 전화번호
from USED_GOODS_BOARD a join USED_GOODS_USER b on a.WRITER_ID=b.USER_ID
group by a.WRITER_ID
having count(*)>=3
order by a.WRITER_ID desc