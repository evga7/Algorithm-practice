-- 코드를 입력하세요
SELECT a.book_id,b.author_name,date_format(a.published_date,'%Y-%m-%d') from book a join author b on a.AUTHOR_ID=b.AUTHOR_ID
where a.category='경제'
order by a.published_date