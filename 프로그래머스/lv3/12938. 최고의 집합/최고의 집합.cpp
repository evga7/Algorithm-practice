#include <bits/stdc++.h>

using namespace std;
vector<int> solution(int n, int s) {
    vector<int> answer;
    if (n > s)
        return { -1 };
    int S = s;
    int N = n;
    int div = s / n;
    int num = 0;
    while (S)
    {
        if (n - answer.size() - (S / (div + 1)) == 0)
        {
            int si = answer.size();
            for (int i = 0; i < n - si; i++)
            {
                answer.push_back(div + 1);
            }
            break;
        }
        S -= div;
        answer.push_back(div);
    }
    sort(answer.begin(), answer.end());
    return answer;
}