#include<bits/stdc++.h>
using namespace std;
vector<int>v;
string solution(string s) {
    string answer = "";
    string temp="";
    for (auto cur :s)
    {
        if (cur==' ')
        {
            v.push_back(stoi(temp));
            temp="";
            continue;
        }
        temp+=cur;
    }
    v.push_back(stoi(temp));
    sort(v.begin(),v.end());
    int l=v.size();
    answer=to_string(v[0])+' '+to_string(v[l-1]);
    return answer;
}