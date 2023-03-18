#include <bits/stdc++.h>
using namespace std;
bool cmp(vector<int>& v1, vector<int>& v2)
{
    return v1.size() < v2.size();
}
vector<int> solution(string s) {
    vector<int> answer;
    vector<vector<int>>v;
    int idx = 2;
    int len = s.size();
    int v_idx = 0;
    int num;
    vector<int>temp;
    while (idx+1<len)
    {
        num = 0;
        if (isdigit(s[idx]))
        {
            num = s[idx] - '0';
            while (1)
            {
                idx++;
                if (isdigit(s[idx]))
                    num = num * 10 + s[idx] - '0';
                else
                    break;
            }
        }
        if (num != 0)
            temp.push_back(num);
        if (s[idx] == '}')
        {
            v.push_back(temp);
            temp.clear();
        }
        idx++;
    }
    sort(v.begin(), v.end(), cmp);
    int i;
    set<int>st;
    for (i = 0; i <v.size(); i++)
    {
        for (auto num : v[i])
        {
            auto it = st.find(num);
            if (it==st.end())
            {
                st.insert(num);
                answer.push_back(num);
            }
        }
    }
    for (auto num : answer)
        cout << num << " ";
    return answer;
}