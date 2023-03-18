#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
priority_queue<int, vector<int>, greater<int>>q1, q2;
int solution(vector<int> A, vector<int> B) {
	int answer = 0;
    int i;
    for (i=0;i<A.size();i++)
    {
        q1.push(A[i]);
        q2.push(B[i]);
    }
    while(!q1.empty()&&!q2.empty())
    {
        if (q1.top()<q2.top())
        {
            answer++;
            q1.pop();
        }
        q2.pop();
    }
    return answer;
}