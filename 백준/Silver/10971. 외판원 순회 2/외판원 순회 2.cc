#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000000
#define pb push_back
#define pob pop_back
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
int res = MAX;
int num, num2;
int T;
int K;
int L;
queue<pair<int,char>>op;
int arr[11][11];
int visited[11];
void solve(int start,int next,int sum,int cnt)
{
	if (start == next&&cnt==N)
	{
		res = min(res, sum);
		return;
	}
	int i;
	if (!visited[next])
	{
		visited[next] = 1;
		for (i = 0; i < N; i++)
		{
			if (arr[next][i])
			{
				solve(start, i, sum + arr[next][i], cnt + 1);
			}
		}
		visited[next] = 0;
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			cin >> arr[i][j];
	for (i = 0; i < N; i++)
	{
		solve(i, i, 0, 0);
	}
	cout << res;
}




