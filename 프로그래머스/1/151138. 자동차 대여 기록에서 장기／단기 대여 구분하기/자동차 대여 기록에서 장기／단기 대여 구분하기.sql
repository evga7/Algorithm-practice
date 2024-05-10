-- 코드를 입력하세요
SELECT HISTORY_ID,CAR_ID,date_format(START_DATE,'%Y-%m-%d') as START_DATE,
date_format(end_date,'%Y-%m-%d') as END_DATE,
if ( datediff(END_DATE,start_date)>=29,'장기 대여','단기 대여') RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where START_DATE like '2022-09%'
order by history_id desc