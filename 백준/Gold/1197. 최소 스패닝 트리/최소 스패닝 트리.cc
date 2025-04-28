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
int res;
int N, M, T;
int num;
string str;
//왼 위 오 아래
int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };
typedef struct info
{
	int cost, x, y;
}info;
vector<info>v;
int parent[10001];
bool cmp(const info& i1, const info& i2)
{
	return i1.cost < i2.cost;
}
int find(int x)
{
	if (x == parent[x])return x;
	return parent[x] = find(parent[x]);
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
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M;
	int a, b, c;
	for (int i = 0; i < M; i++)
	{
		cin >> a >> b >> c;
		v.push_back({ c,a,b });
	}
	sort(v.begin(), v.end(),cmp);
	for (int i = 1; i <= N; i++)
		parent[i] = i;
	for (auto cur : v)
	{
		if (uni(cur.x, cur.y))
			res += cur.cost;
	}
	cout << res;

}



