-- 코드를 입력하세요
SELECT a.NAME,a.DATETIME from animal_ins a left join animal_outs b on a.ANIMAL_ID=b.ANIMAL_ID
where b.name is null and a.name is not null
order by a.DATETIME limit 3