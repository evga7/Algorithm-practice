#include<bits/stdc++.h>
using namespace std;

priority_queue<int>pq;
long long solution(int n, vector<int> works) {
    long long answer = 0;
    for (auto cur : works)
    {
        pq.push(cur);
    }
    while (!pq.empty() && n)
    {
        int top = pq.top()-1;
        pq.pop();
        if (top)
            pq.push(top);
        n -= 1;
    }
    while (!pq.empty()) {
        answer += pow(pq.top(), 2);
        pq.pop();
    }
    return answer;
}