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
int m[201][201];
vec v;
int parent[201];
bool is_inside(int x, int y)
{		
	if (x >= N || x < 0 || y < 0 || y >= M)return false;
	return true;
}

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
		parent[y] = x;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	for (i = 1; i <= N; i++)
		parent[i] = i;
	for (i = 1; i <=N; i++)
	{
		for (j = 1; j <=N; j++)
		{
			cin >> num;
			if (num)
				uni(i, j);
		}
	}
	cin >> num;
	int chk = find(num);
	for (i = 1; i < M; i++)
	{		cin >> num;
		if (chk != find(num))
		{
			cout << "NO";
			return 0;
		}
	}
	cout << "YES";
}
