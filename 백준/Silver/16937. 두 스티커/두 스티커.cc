#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD  1000000009
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef pair<string, int> psi;
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<ll> vecll;
typedef vector<pii> vpi;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
int L;
int res;
int N, M, T;
ll num;
int t;
int K;
int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };
vpi vp;
vec v;
bool visited[101];
struct info {
	int x, y, idx;
};
void chk(pii p1,pii p2)
{
	int x1 = p1.first;
	int y1 = p1.second;
	int x2 = p2.first;
	int y2 = p2.second;
	int s =( p1.first * p1.second )+ (p2.first * p2.second);
	if (x1 + x2 <= N)
	{
		if (max(y1, y2) <= M)
			res = max(s, res);
	}
	else if (y1 + y2 <=  M)
	{
		if (max(x1, x2) <= N)
			res = max(s, res);
	}
}
void go()
{
	vector<info> vp2;
	vpi vp3;
	for (auto cur : v)
	{
		vp3.push_back(vp[cur]);
	}
	int idx = 0;
	for (auto cur : vp3)
	{
		if (cur.first != cur.second)
		{
			vp2.push_back({ cur.first,cur.second,idx});
			vp2.push_back({ cur.second,cur.first,idx });
		}
		else
			vp2.push_back({cur.first,cur.second,idx});
		idx++;
	}
	for (int i = 0; i < vp2.size(); i++)
	{
		for (int j = i + 1; j < vp2.size(); j++)
		{
			auto c1 = vp2[i];
			auto c2 = vp2[j];
			if (c1.idx!=c2.idx)
				chk({ c1.x,c1.y }, { c2.x,c2.y });
		}
	}
}
void solve(int idx, int cnt)
{
	if (cnt == 2)
	{
		int s = 0;
		go();
		return;
	}
	for (int i = idx; i < T; i++)
	{
		v.push_back(i);
		solve(i + 1, cnt + 1);
		v.pop_back();
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M;
	cin >> T;
	int a, b;
	for (int i=0;i<T;i++)
	{
		cin >> a >> b;
		vp.push_back({ a,b });
	}
	solve(0,0);
	cout << res;
}
