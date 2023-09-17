select PT_NAME,PT_NO,GEND_CD,AGE,if(TLNO is null,'NONE',TLNO) TLNO from patient
where age<=12 and GEND_CD='W'
order by age desc,pt_name asc