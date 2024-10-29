#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef pair<int, char> pi4;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int num;
int res = 0;
int D, K,C;
deque<pi>dq;
int visited[3001];
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> D >> K >> C;
	for (i = 0; i < N; i++)
	{
		cin >> num;
		dq.push_back({ 0,num });
	}
	while (1)
	{
		int cnt = 0;
		for (i = 0; i < K; i++)
		{
			int& ret = visited[dq[i].second];
			if (!ret)
			{
				ret = 1;
				cnt++;
			}
		}
		if (!visited[C])cnt++;
		res = max(res, cnt);
		memset(visited, 0, sizeof(visited));
		if (dq.front().first)break;
		else
		{
			auto t = dq.front();
			t.first = 1;
			dq.pop_front();
			dq.push_back(t);
		}

	}
	cout << res;
}