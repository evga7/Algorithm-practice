#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vvi;
typedef vector<pii>vpi;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef queue<pii> que;
typedef vector<vector<pii>> gra;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int res;
int num;
vec v;
vec v2;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}
	for (int i = 1; i < N; i++)
	{
		v2.push_back(v[i] - v[i - 1]);
	}
	sort(v2.begin(), v2.end());
	for (int i = 0; i < N - M; i++)
		res += v2[i];
	cout << res;

}