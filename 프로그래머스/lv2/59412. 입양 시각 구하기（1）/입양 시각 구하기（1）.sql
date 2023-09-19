-- 코드를 입력하세요
SELECT hour(DATETIME) HOUR,count(DATETIME) count from animal_outs
group by HOUR
having HOUR>=9 and HOUR<20
order by HOUR