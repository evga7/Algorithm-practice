#include <string>
#include <vector>
#include <queue>
using namespace std;
int solution(vector<int> scoville, int K) {
	int answer = 0;
	int i;
	priority_queue<int, vector<int>, greater<int>> pq;
	for (i = 0; i < scoville.size(); i++)
		pq.push(scoville[i]);
	while (pq.top()<=K)
	{
        if(pq.size()<=1)
            return -1;
		else 
		{
			int a, b,c;
			a = pq.top();
			pq.pop();
			b = pq.top();
			pq.pop();
            c=a+(b*2);
			pq.push(c);
			answer++;
		}
	}
	return answer;
}