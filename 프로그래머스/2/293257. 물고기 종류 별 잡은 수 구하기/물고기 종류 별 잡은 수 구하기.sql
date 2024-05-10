-- 코드를 작성해주세요
select count(*) FISH_COUNT,b.FISH_NAME from FISH_INFO a join fish_name_info b on a.fish_type=b.fish_type
group by a.fish_type,b.fish_name
order by FISH_COUNT desc