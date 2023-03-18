#include <string>
#include <vector>
#include <queue>
using namespace std;
priority_queue<int> pq;
queue<pair<int, int>>q;
int solution(vector<int> priorities, int location) {
	int answer = 0;
	for (int i = 0; i < priorities.size(); i++)
	{
		q.push(make_pair(priorities[i], i));
		pq.push(priorities[i]);
	}
	int cnt = 0;
	while (!q.empty())
	{
		int x, y;
		x = q.front().first;
		y = q.front().second;
		q.pop();
		if (x == pq.top())
		{
			pq.pop();
			cnt++;
			if (y == location)
			{
				answer = cnt;
				break;
			}
		}
		else
		{
			q.push(make_pair(x, y));
		}
	}
	printf("%d", answer);
	return answer;
}