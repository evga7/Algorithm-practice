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
typedef vector<vector<pi>> gra;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int res;
int num;
vector<int>v;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	v.push_back(-MAX);
	for (i = 0; i <N; i++)
	{
		cin >> num;
		if (num > v.back())
		{
			v.push_back(num);
			res++;
		}
		else
		{
			auto it = lower_bound(v.begin(), v.end(), num);
			*it = num;
		}
	}
	//memset(dp, -1, sizeof(dp));
	
	cout << res;
}


