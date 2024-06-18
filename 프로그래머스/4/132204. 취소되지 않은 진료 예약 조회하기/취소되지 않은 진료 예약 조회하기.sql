-- 코드를 입력하세요
SELECT c.APNT_NO,a.PT_NAME,a.PT_NO,c.MCDP_CD,b.DR_NAME,c.APNT_YMD from DOCTOR b join APPOINTMENT  c on b.DR_ID=c.MDDR_ID
join PATIENT a on a.PT_NO=c.PT_NO
where c.MCDP_CD ='CS' and c.APNT_YMD like '%2022-04-13%' and c.APNT_CNCL_YMD is null
order by c.APNT_YMD