-- 코드를 입력하세요
SELECT a.NAME,a.DATETIME from ANIMAL_INS a left outer join ANIMAL_OUTS b on a.ANIMAL_ID=b.ANIMAL_ID
where a.NAME is not null and b.name is null
order by a.DATETIME limit 3