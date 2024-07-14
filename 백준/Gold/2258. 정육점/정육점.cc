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
int res = MAX;
int L, P;
vec2 v;
bool is_inside(int x, int y)
{		
	if (x >= N || x < 0 || y < 0 || y >= M)return false;
	return true;
}
bool cmp(pi& p1, pi& p2)
{
	if (p1.first == p2.first) return p1.second > p2.second;
	return p1.first < p2.first;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	int a, b;
	for (i = 0; i < N; i++)
	{
		cin >> a >> b;
		v.push_back({ b,a });
	}
	sort(v.begin(), v.end(),cmp);
	int w = 0;
	int s = 0;
    int flag=0;
	for (i = 0; i < N; i++)
	{
		w += v[i].second;
		if (i > 0 && v[i].first == v[i - 1].first)
			s += v[i].first;
		else
			s = 0;
		if (w >= M)
        {
			res = min(res, v[i].first + s);
            flag=1;
        }
	}
	if (!flag)
		res = -1;
	cout << res;
}
