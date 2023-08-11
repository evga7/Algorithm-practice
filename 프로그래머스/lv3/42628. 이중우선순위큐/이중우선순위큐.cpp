#include <bits/stdc++.h>

using namespace std;
multiset<int>mq;
vector<int> solution(vector<string> operations) {
    vector<int> answer;
    for (auto cur : operations)
    {
        char op;
        op=cur[0];
        string s = cur.substr(2);
        int num = stoi(s);
        if (op=='I')
        {
            mq.insert(num);
        }
        else if (op=='D' && mq.size())
        {
            if (num==-1){
                mq.erase(mq.begin());
            }
            else{
                mq.erase(--mq.end());
            }
        }
    }
    if (mq.size()>1)
        return {*--mq.end(),*mq.begin()};
    return {0,0};
}