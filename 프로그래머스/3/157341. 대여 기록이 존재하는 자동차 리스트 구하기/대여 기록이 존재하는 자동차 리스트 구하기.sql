-- 코드를 입력하세요
SELECT a.CAR_ID from CAR_RENTAL_COMPANY_CAR a join CAR_RENTAL_COMPANY_RENTAL_HISTORY b on a.CAR_ID=b.CAR_ID
where a.CAR_TYPE='세단' and b.START_DATE like '2022-10%'
group by CAR_ID
order by CAR_ID desc