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
typedef tuple<int, int, int> tup;
typedef vector<vector<pi>> gra;
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };
ll N, M;
int T;
int K;
int res;
int num, num2;
string str;
bool is_inside(int x, int y)
{
	return x >= 0 && x < N&& y >= 0 && y < N;
}
bool chk(string& s)
{
	int cnt = 0;
	for (auto cur : s)
	{
		if (cur == '5')
			cnt += 1;
		if (cnt >= M)
			return true;
	}
	return false;
}
void go(string s, int pos)
{
	ll num = stoll(s);
	if (chk(s) && num>N)
	{
		cout << s;
		exit(0);
	}
	while (s[pos] == '5' && pos - 1 >= 0)
		pos -= 1;
	ll nxt_num = num + pow(10, s.length() - pos - 1);
	string nxt = to_string(nxt_num);
	go(nxt, nxt.length() - 1);
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M;
	string s = to_string(N + 1);
	go(s, s.length()-1);


}

