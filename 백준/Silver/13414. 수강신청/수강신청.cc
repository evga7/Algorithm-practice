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
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef vector<vector<pi>> gra;
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,1,0,-1 };
int N, M;
int L;
int T;
int res;
int num, num2;
int sum;
string str;
map<string,int>m;
vector<pair<int, string>>v;
bool cmp(pair<string, int> & p1, pair<string, int> & p2)
{
	return p1.second < p2.second;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	for (i = 0; i < M; i++)
	{
		cin >> str;
		m[str] = i;
	}
	for (auto it : m)
		v.push_back({ it.second,it.first});
	sort(v.begin(), v.end());
	if (N > v.size())
		for (auto it : v)
			cout << it.second << "\n";
	else
		for (i = 0; i < N; i++)
			cout << v[i].second << "\n";
}







