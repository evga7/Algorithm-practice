#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000009
#define pb push_back
#define pob pop_back
#define ms memset
#define FOR(i,a,b) for(int i = a; i < b; i++)
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef vector<vector<pi>> gra;
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };
int N, M;
int T;
int res;
int num, num2;
int arr[1001][1001];
int parent[1001];
vector<pi2> graph;
vec2 v;
int find(int x)
{
	if (parent[x] == x)return x;
	return parent[x] = find(parent[x]);
}
int uni(int x, int y)
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
	int i, j;
	cin >> N >> M;
	for (i = 1; i <= N; i++)
	{
		parent[i] = i;
	}
	for (i = 0; i < M; i++)
	{
		cin >> num >> num2;
		uni(num, num2);
	}
	FOR(i, 1, N + 1)
	{
		FOR(j, 1, N + 1)
		{
			cin >> num;
			if (i != 1 && j != 1)graph.push_back({ num,{i,j } });
		}
	}
	sort(graph.begin(), graph.end());
	for (auto next : graph)
	{
		int x = next.second.first;
		int y = next.second.second;
		int cost = next.first;
		if (uni(x, y))
		{
			res += cost;
			v.push_back({ x, y });
		}
	}
	cout << res << " " << v.size() << "\n";
	for (auto a : v)
	{
		cout << a.first << " " << a.second << "\n";
	}
}





