-- 코드를 입력하세요
SELECT user_id,nickname,sum(a.price) TOTAL_SALES from used_goods_board a join used_goods_user b on a.writer_id=b.user_id 
where a.status ='DONE' 
group by user_id
having TOTAL_SALES>=700000
order by TOTAL_SALES