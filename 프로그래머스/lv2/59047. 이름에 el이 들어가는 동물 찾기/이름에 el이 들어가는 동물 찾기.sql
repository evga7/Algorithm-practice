-- 코드를 입력하세요
SELECT ANIMAL_ID,NAME from animal_ins
where lower(name) like '%el%' and ANIMAL_TYPE = 'Dog'
order by name