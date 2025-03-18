-- 코드를 작성해주세요
select a.DEPT_ID,a.DEPT_NAME_EN,round(avg(b.SAL)) AVG_SAL from HR_DEPARTMENT a join HR_EMPLOYEES b on a.DEPT_ID=b.DEPT_ID
group by a.dept_id,a.DEPT_NAME_EN
order by AVG_SAL desc