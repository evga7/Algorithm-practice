-- 코드를 입력하세요
SELECT MEMBER_ID,MEMBER_NAME,GENDER,date_format(DATE_OF_BIRTH,'%Y-%m-%d') DATE_OF_BIRTH from MEMBER_PROFILE 
where TLNO is not null and month(DATE_OF_BIRTH) = '03' and GENDER ='W'
order by member_id