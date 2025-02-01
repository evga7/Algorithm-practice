#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
#define pb push_back
#define pob pop_back
#define FOR(i,a,b) for(int i = a; i < b; i++)
using namespace std;
typedef long long int ll;
typedef unsigned long long int lll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef vector<vector<pi>> gra;
int dx[4] = { 0, 0,-1,1 };
int dy[4] = { 1,-1,0,0 };
int N, M;
int D;
int T;
int res;
int num, num2;
int sum;
string str;
vec2 v;
map<char, pi>mp;
int dist(char a, char b)
{
	return abs(mp[a].first - mp[b].first) + abs(mp[a].second - mp[b].second);
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	mp['q'] = { 0,0 }, mp['w'] = { 0,1 }, mp['e'] = { 0,2 }, mp['r'] = { 0,3 }, mp['t'] = { 0,4 },
		mp['y'] = { 0,5 }, mp['u'] = { 0,6 }, mp['i'] = { 0,7 }, mp['o'] = { 0,8 }, mp['p'] = { 0,9 },
		mp['a'] = { 1,0 }, mp['s'] = { 1,1 }, mp['d'] = { 1,2 }, mp['f'] = { 1,3 }, mp['g'] = { 1,4 },
		mp['h'] = { 1,5 }, mp['j'] = { 1,6 }, mp['k'] = { 1,7 }, mp['l'] = { 1,8 }, mp['z'] = { 2,0 },
		mp['x'] = { 2,1 }, mp['c'] = { 2,2 }, mp['v'] = { 2,3 }, mp['b'] = { 2,4 }, mp['n'] = { 2,5 },
		mp['m'] = { 2,6 };
	char l, r;
	cin >> l >> r;
	cin >> str;
	res = str.size();
	for (auto cur : str)
	{
		if (cur == l || cur == r)continue;
		int x = mp[cur].first;
		int y = mp[cur].second;
		if ((!x && y >= 0 && y <= 4) ||
			(x == 1 && y >= 0 && y <= 4) ||
			(x == 2 && y >= 0 && y <= 3)) {
			res += dist(l, cur);
			l = cur;
		}
		else
		{
			res += dist(r, cur);
			r = cur;
		}
	}
	cout << res;
}







