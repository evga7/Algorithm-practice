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
int dx[4] = { 0,1,0,-1 }; //오 아래 왼 위
int dy[4] = { 1,0,-1,0 };
int res;
int num;
string str,str2;
int N, M;
vpi v;
map<string, int>m;
bool f;
void solve(int idx,int idx2)
{
	if (f)return;
	if (idx2 == str2.size() - 1)
	{
		if (str[idx] == '*' && (idx + 1) < str.size())
			idx++;
		if (str[idx] == str2[idx2]&&idx==str.size()-1)f = true;
		return;
	}
	if (str[idx] == '*')
	{
		solve(idx, idx2 + 1);
		solve(idx + 1, idx2);
	}
	else if (str[idx] == str2[idx2])
		solve(idx + 1, idx2 + 1);
	
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	cin >> str;
	for (int i = 0; i < N; ++i)
	{
		cin >> str2;
		solve(0,0);
		if (f)cout << "DA";
		else
			cout << "NE";
		cout << "\n";
		f = false;
	}
	
	
}