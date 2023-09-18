-- 코드를 입력하세요
SELECT ANIMAL_ID,NAME,SEX_UPON_INTAKE from animal_ins
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by ANIMAL_ID