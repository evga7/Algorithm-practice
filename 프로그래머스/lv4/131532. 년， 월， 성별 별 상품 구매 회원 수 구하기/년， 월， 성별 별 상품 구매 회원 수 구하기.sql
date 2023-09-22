SELECT year(b.SALES_DATE) YEAR,month(b.SALES_DATE) MONTH ,a.GENDER GENDER,count(distinct(b.USER_ID)) USERS from USER_INFO a join ONLINE_SALE b on a.USER_ID=b.USER_ID
where gender is not null
group by YEAR,MONTH,gender
order by YEAR,MONTH,GENDER