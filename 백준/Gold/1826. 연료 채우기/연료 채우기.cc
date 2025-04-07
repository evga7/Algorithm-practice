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
int res;
int L, P;
priority_queue<int>pq;
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
	cin >> N;
	int a, b;
	for (i = 0; i < N; i++)
	{
		cin >> a >> b;
		v.push_back({ a,b });
	}
	int idx = 0;
	sort(v.begin(), v.end());
	cin >> L >> P;
	while (P<L)
	{
		if (idx >= L || !P)break;
		
		while (idx < N && v[idx].first<= P)
		{
			int oil = v[idx].second;
			pq.push(oil);
			idx++;
		}
		if (pq.empty())break;
		P += pq.top();
		pq.pop();
		res++;
	}
	if (P < L)
		res = -1;
	cout << res;

}
