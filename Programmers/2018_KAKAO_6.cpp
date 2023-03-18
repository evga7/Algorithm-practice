#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int tt(string s)
{
    string ti = s.substr(0, 2);
    string mi = s.substr(3, 2);
    return stoi(ti) * 60 + stoi(mi);
}
string solution(int n, int t, int m, vector<string> timetable) {
    string answer = "";
    vector<int>table;
    int i,j;
    for (i = 0; i < timetable.size(); i++)
    {
        int ti = tt(timetable[i]);
        table.push_back(ti);
    }
    sort(table.begin(), table.end());
    int start = 540;
    int idx = 0;
    int res = 0;
    int len = table.size();
    for (i = 0; i < n; i++)
    {
        int f = m;
        for (j = idx; j < len; j++)
        {
            if (table[j] <= start)
            {
                f--;
                idx++;
                if (f == 0)
                    break;
            }
        }
        if (i + 1 == n)
        {
            if (f == 0)
                res = table[idx- 1] - 1;
            else
            {
                res = start;
            }
        }
        start += t;
        if (start >= 60 * 24)break;
    }
    string temp="";
    int T = res / 60;
    int S = res % 60;
    if (T < 10)
        temp = temp + '0' + to_string(T);
    else
        temp = temp + to_string(T);
    temp = temp + ':';
    if (S < 10)
        temp = temp + '0' + to_string(S);
    else
        temp = temp + to_string(S);
    answer = temp;
    return answer;
}