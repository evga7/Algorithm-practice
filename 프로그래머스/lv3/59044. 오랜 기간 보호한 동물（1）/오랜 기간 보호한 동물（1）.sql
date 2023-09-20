-- 코드를 입력하세요
SELECT a.NAME,a.DATETIME DATETIME from ANIMAL_INS a left join ANIMAL_OUTS b on a.ANIMAL_ID=b.ANIMAL_ID
where b.ANIMAL_ID is null
order by DATETIME limit 3