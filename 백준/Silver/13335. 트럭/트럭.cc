#include <bits/stdc++.h>
#include <unordered_map>
#define MAX 1000000001
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };
int N, W, L;
int res;
vector<int>v;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N>>W>>L;
	int i;
	int num;
	for (i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}
	queue<int>q;
	deque<int>times;
	int sum = 0;
	int idx = 0;
	int cnt = 0;
	while (1)
	{
		for (auto& num : times)
		{
			num++;
			if (num >=W)
			{
				times.pop_front();
				sum -= q.front();
				q.pop();
				cnt++;
			}
		}

		if (idx<N&&sum + v[idx] <= L)
		{
			q.push(v[idx]);
			times.push_back(0);
			sum += v[idx];
			idx++;
		}
		res++;
		if (cnt == N)
			break;
	}
	cout << res;
}
