-- 코드를 입력하세요
SELECT b.AUTHOR_ID,b.AUTHOR_NAME,a.CATEGORY,sum(a.price*c.sales) TOTAL_SALES from BOOK a join AUTHOR b on a.AUTHOR_ID=b.AUTHOR_ID
join BOOK_SALES c on a.BOOK_ID=c.BOOK_ID
where c.SALES_DATE like '%2022-01%'
group by b.AUTHOR_NAME,a.CATEGORY
order by b.AUTHOR_ID,a.CATEGORY desc