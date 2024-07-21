#include <bits/stdc++.h>
#define MAX 2147483647
#define MIN -2147483,648
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vpi;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int num;
int res;
int T;
vec2 v;
bool is_inside(int x, int y)
{
	if (x >= N || x < 0 || y < 0 || y >= M)return false;
	return true;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	int N;
	cin >> T;
	while (T--)
	{
		cin >> N;
		int a, b;
		res = 1;
		v.clear();
		for (i = 0; i < N; i++)
		{
			cin >> a >> b;
			v.push_back({ a,b });
		}
		sort(v.begin(), v.end());
		int m = v.front().second;
		for (i = 1; i < N; i++)
		{
			if (m > v[i].second)
			{
				m = v[i].second;
				res++;
			}
		}
		cout << res << "\n";
	}
}
