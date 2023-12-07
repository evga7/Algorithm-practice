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
typedef vector<vector<pi>> gra;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int res;
int num;
vec v;
vec v2;
int visited[9];

void solve(int cnt,int idx)
{
	if (cnt == M)
	{
		for (auto a : v2)
		{
			cout << a << " ";
		}
		cout << "\n";
		return;
	}
	int i;
	int back = -777;
	for (i = idx; i < N; i++)
	{
		if (!visited[i]&&back!=v[i])
		{
			visited[i] = 1;
			v2.push_back(v[i]);
			back = v[i];
			solve(cnt + 1,i+1);
			visited[i] = 0;
			v2.pop_back();
		}
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	for (i = 0; i < N; i++)
		cin >> num, v.push_back(num);
	sort(v.begin(), v.end());
	solve(0,0);
}



