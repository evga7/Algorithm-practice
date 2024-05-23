-- 코드를 입력하세요
SELECT a.CATEGORY CATEGORY,sum(b.sales) TOTAL_SALES from BOOK a join BOOK_SALES b on a.book_id=b.book_id
where SALES_DATE like '%2022-01%'
group by CATEGORY
order by CATEGORY