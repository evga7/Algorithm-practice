#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
int dx[4] = { 0, 0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int N, M, T;
int K;
int res;
ll num, num2;
typedef pair<int, int> pii;
int parent[1001];
struct info {
	int dir, x, y;
};
vector<info>v;
int find(int x)
{
	if (x == parent[x])return x;
	else return parent[x] = find(parent[x]);
}
bool cmp(info& v1, info& v2)
{
	return v1.dir < v2.dir;
}
bool cmp2(info& v1, info& v2)
{
	return v1.dir > v2.dir;
}
bool uni(int x, int y)
{
	x = find(x);
	y = find(y);
	if (x != y)
	{
		parent[y] = x;
		return true;
	}
	return false;
}
int solve()
{
	int cnt = 0;
	for (auto cur : v)
	{
		int x, y;
		x = cur.x;
		y = cur.y;
		if (uni(x, y))
		{
			if (cur.dir == 0)cnt++;
		}
	}
	return cnt * cnt;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	int a, b, c;
	for (i = 0; i <=M; i++)
	{
		cin >> a >> b >> c;
		v.push_back({ c,a,b });
	}
	sort(v.begin(), v.end(), cmp);
	for (i = 0; i <= N; i++)
		parent[i] = i;
	res = solve();
	sort(v.begin(), v.end(), cmp2);
	for (i = 0; i <= N; i++)
		parent[i] = i;
	res -= solve();
	cout << res;

}


