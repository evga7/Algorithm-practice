-- 코드를 입력하세요
SELECT hour(datetime) hour ,count(datetime) from ANIMAL_OUTS 
where hour(datetime)>=9 and hour(datetime)<20
group by hour
order by hour(datetime)