-- 코드를 입력하세요
SELECT HISTORY_ID,CAR_ID,date_format(start_DATE,'%Y-%m-%d'),date_format(END_DATE,'%Y-%m-%d'),
if (datediff(end_date,start_date)>=29,'장기 대여','단기 대여') as 'RENT_TYPE'
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date>='2022-09-01' and start_date<='2022-09-30'
order by history_id desc