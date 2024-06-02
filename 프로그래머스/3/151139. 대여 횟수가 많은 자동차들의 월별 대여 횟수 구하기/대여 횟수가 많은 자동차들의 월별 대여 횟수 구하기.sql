-- 코드를 입력하세요
select MONTH(start_date) MONTH,car_id,count(car_id) RECORDS from car_rental_company_rental_history
where date_format(start_date,'%Y-%m') between '2022-08' and '2022-10'
and
car_id in (
SELECT car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where date_format(start_date,'%Y-%m') between '2022-08' and '2022-10='
    group by car_id
    having count(car_id)>=5
)
group by MONTH,car_id
having RECORDS>0
order by MONTH,car_id desc