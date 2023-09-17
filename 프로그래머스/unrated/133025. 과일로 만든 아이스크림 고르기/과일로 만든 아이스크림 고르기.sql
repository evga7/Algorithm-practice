
SELECT (a.FLAVOR) from FIRST_HALF as a inner join ICECREAM_INFO as b on a.flavor=b.flavor
where a.TOTAL_ORDER>=3000 and b.INGREDIENT_TYPE ='fruit_based'
order by TOTAL_ORDER desc