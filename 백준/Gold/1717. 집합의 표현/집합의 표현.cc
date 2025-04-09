#include <bits/stdc++.h>
#define MAX 2147483647
#define MIN -2147483648
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
int res;
int num;
vec v;
int parent[1000001];
int find(int x)
{
	if (parent[x] == x)return x;
	return parent[x] = find(parent[x]);
}
void uni(int x, int y)
{
	x = find(x);
	y = find(y);
	if (x != y)
	{
		parent[y] = x;
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cout.tie(0);
	int i, j;
	cin >> N >> M;
	int a, b, c;
	for (i = 1; i <= N; i++)
		parent[i] = i;
	for (i = 0; i < M; i++)
	{
		cin >> a >> b >> c;
		if (a == 1)
		{
			if (find(b)==find(c))
				cout << "YES" << "\n";
			else
				cout << "NO" << "\n";
		}
		else
			uni(b, c);
	}
}



