-- 코드를 입력하세요
SELECT a.flavor from first_half as a inner join ICECREAM_INFO as b on a.flavor=b.flavor
where a.total_order>=3000 and b.INGREDIENT_TYPE like '%fruit%'
order by a.total_order desc