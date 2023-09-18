-- 코드를 입력하세요
SELECT distinct(a.car_id) from CAR_RENTAL_COMPANY_CAR a join CAR_RENTAL_COMPANY_RENTAL_HISTORY b on a.CAR_ID=b.car_id
where a.CAR_TYPE='세단' and b.START_DATE like '%2022-10%'
order by car_id desc