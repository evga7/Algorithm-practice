#include <bits/stdc++.h>
using namespace std;
vector<char>v;
vector<string> d;
bool chk() {
    for (auto cur : d)
    {
        char a = cur[0];
        char b = cur[2];
        char op = cur[3];
        int num = cur[4]-'0';
        int cal = abs( (find(v.begin(), v.end(), a)-v.begin()) - (find(v.begin(), v.end(), b)-v.begin()))-1;
        if (op == '=')
        {
            if (num != cal)
                return false;
        }
        else if (op == '>')
        {
            if (num >= cal)
                return false;
        }
        else
        {
            if (num <= cal)
                return false;
        }
    }
    return true;
}
bool visited[9];
int res;
vector<char>a;
void go(int cnt)
{
    if (cnt == 8)
    {
        if (chk())
            res += 1;
        return;
    }
    for (int i = 0; i < 8; i++)
    {
        if (visited[i])continue;
        visited[i] = 1;
        v.push_back(a[i]);
        go(cnt + 1);
        visited[i] = 0;
        v.pop_back();
    }
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vector<string> data) {
    res = 0;
    d = data;
    for (int i = 0; i < 9; i++)
        visited[i] = 0;
    a = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
    go(0);
    return res;
}