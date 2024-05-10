-- 코드를 입력하세요
select a.TITLE,a.BOARD_ID,b.REPLY_ID,b.WRITER_ID,b.CONTENTS,
date_format(b.CREATED_DATE,'%Y-%m-%d') CREATED_DATE
from USED_GOODS_BOARD a join USED_GOODS_REPLY b on a.board_id=b.board_id
where a.CREATED_DATE like '2022-10%'
order by b.CREATED_DATE,a.title