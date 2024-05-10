-- 코드를 작성해주세요
select b.ID,b.EMAIL,b.FIRST_NAME,b.LAST_NAME from DEVELOPERS b
where b.skill_code & (select code from skillcodes where name like '%Python%') or 
b.skill_code & (select code from skillcodes where name like '%C#%')
order by b.id