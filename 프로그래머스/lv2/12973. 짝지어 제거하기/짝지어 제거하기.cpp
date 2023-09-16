#include<bits/stdc++.h>
using namespace std;
int solution(string s)
{
    int answer = 0;
    stack<char>st;
    for (auto cur:s)
    {
        if (!st.empty()&&st.top()==cur)
        {
            st.pop();
            continue;
        }
        st.push(cur);
    }
    if (st.size())
        return 0;
    return 1;
}