-- 코드를 입력하세요
SELECT a.CATEGORY ,sum(b.sales) TOTAL_SALES from book a join BOOK_SALES b on a.book_id=b.book_id
where b.SALES_DATE like '%2022-01%'
group by a.CATEGORY
order by a.CATEGORY