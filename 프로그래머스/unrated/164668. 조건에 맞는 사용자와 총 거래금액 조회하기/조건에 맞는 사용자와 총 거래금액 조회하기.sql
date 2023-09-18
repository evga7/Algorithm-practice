-- 코드를 입력하세요
SELECT b.USER_ID,b.NICKNAME,sum(price) TOTAL_SALES from USED_GOODS_BOARD a join USED_GOODS_USER b on a.WRITER_ID=b.USER_ID
where a.STATUS='DONE'
group by b.user_id
having TOTAL_SALES>=700000
order by TOTAL_SALES