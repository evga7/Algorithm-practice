-- 코드를 입력하세요
SELECT DR_NAME,DR_ID,MCDP_CD,date_format(HIRE_YMD,'%Y-%m-%d') HIRE_YMD from doctor
where MCDP_CD='CS' or MCDP_CD='GS'
order by hire_ymd desc,dr_name