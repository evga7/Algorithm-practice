#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
int dx[4] = { 0, 0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int N, M, T;
int S;
int K;
ll res;
int num, num2;
string str;
vector<ll>s;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	s.resize(N+1);
	for (i = 1; i <=N; i++)
	{
		cin >> s[i];
		s[i] +=s[i - 1];
	}
	for (i = 0; i < M; i++)
	{
		cin >> num;
		auto it = upper_bound(s.begin(), s.end() , num)-s.begin()-1;
		cout << it << "\n";
	}
}