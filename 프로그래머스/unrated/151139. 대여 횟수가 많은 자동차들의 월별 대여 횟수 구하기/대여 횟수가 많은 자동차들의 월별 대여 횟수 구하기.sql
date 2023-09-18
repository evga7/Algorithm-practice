-- 코드를 입력하세요
SELECT month(start_date) MONTH,CAR_ID ,count(*) RECORDS from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where date_format(start_date,'%Y-%m') between '2022-08' and '2022-10'
and car_id in (select CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
               where date_format(start_date,'%Y-%m') between '2022-08' and '2022-10'
               group by CAR_ID 
               having count(car_id)>=5)
group by car_id,MONTH(start_date)
having RECORDS>0
order by MONTH, car_id desc