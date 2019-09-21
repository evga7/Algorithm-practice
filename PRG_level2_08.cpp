#include <string>
#include <vector>
#include <queue>
#include <list>
using namespace std;
int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int answer = 0;
	list<pair<int, int>>l;
	queue<int> weight_q;
	queue<pair<int, int>>q;
	for (auto num : truck_weights)
	{
		q.push(make_pair(num, 0));
	}
	int cnt = 0;
	int cur_weight = weight;

	while (!q.empty() || !l.empty())
	{
		if (!l.empty()&&l.front().second == bridge_length)
		{
			weight += weight_q.front();
			l.pop_front();
			weight_q.pop();
		}

		if (!q.empty() && q.front().first <= weight)
		{
			weight_q.push(q.front().first);
			weight -= q.front().first;
			l.push_back(make_pair(q.front().first, 0));
			q.pop();
		}
		for (auto &a : l)
		{
			a.second++;
		}
		cnt++;
	}
	answer = cnt;
	printf("%d", answer);
	return answer;
}