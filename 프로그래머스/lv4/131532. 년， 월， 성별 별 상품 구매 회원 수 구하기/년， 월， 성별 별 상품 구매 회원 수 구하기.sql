-- 코드를 입력하세요
SELECT year(b.SALES_DATE) YEAR,month(b.SALES_DATE) MONTH,a.GENDER,count(distinct(a.user_id)) USERS from USER_INFO a join ONLINE_SALE b on a.USER_ID=b.USER_ID
where GENDER is not null
group by YEAR,MONTH,GENDER
order by YEAR,MONTH,GENDER