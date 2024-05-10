-- 코드를 작성해주세
select count(*) FISH_COUNT from fish_info a join FISH_NAME_INFO b on a.FISH_TYPE=b.FISH_TYPE
where b.fish_name='BASS' or b.fish_name='SNAPPER'