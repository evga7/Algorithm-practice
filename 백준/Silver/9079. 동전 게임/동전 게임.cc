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
vec v;
int arr[8] = { 448,56,7,292,146,73,273,84 };
bool visited[512];
typedef struct info {
	int num, cnt;
};
int conv()
{
	int sss = 0;
	int ss = 1;
	reverse(str.begin(),str.end());
	for (auto cur : str)
	{
		if (cur == '1')
			sss += ss;
		ss *= 2;
	}
	return sss;
}
void solve()
{
	int s=conv();
	int bit = 0;
	queue<info>q;
	q.push({s,0 });
	visited[s];
	while (!q.empty())
	{
		int cnt = q.front().cnt;
		int num = q.front().num;
		if (num == 511 || num == 0)
			res = min(res, cnt);
		q.pop();
		for (int i = 0; i < 8; i++)
		{
			int n_num = num ^ arr[i];
			if (visited[n_num])continue;
			visited[n_num] = 1;
			q.push({n_num,cnt+1 });
		}
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> T;
	while (T--)
	{
		res = INT_MAX;
		char c;
		str.clear();
		memset(visited, 0, sizeof(visited));
		for (int i = 0; i < 3*3; i++)
		{
			cin >> c;
			if (c == 'H')
				str.push_back('0');
			else
				str.push_back('1');
		}
		solve();
		if (res == INT_MAX)
			res = -1;
		cout << res<<"\n";
	}


}



