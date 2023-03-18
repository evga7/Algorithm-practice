#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
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
ll res;
vector<ll>v;
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
	cin >> N >> M;
	for (i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}
	ll left = 0;
	ll right = 2000000001;
	while (left <= right)
	{
		ll mid = left + right >> 1;
		ll sum = 0;
		for (i = 0; i < N; i++)
		{
			if (mid < v[i])
				sum += v[i] - mid;
		}
		if (M<= sum)
		{
			res = max(res, mid);
			left = mid + 1;
		}
		else
			right = mid - 1;
	}
	cout << res;
}
