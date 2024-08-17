#include<bits/stdc++.h>

using namespace std;
int cnt;
bool solution(string s)
{
    bool answer = true;
    for (auto cur : s)
    {
        if (cur==')')
        {
            if (!cnt)
                return false;
            cnt-=1;
            continue;
        }
        cnt+=1;
    }
    if (cnt>0)
        answer=false;
    return answer;
}