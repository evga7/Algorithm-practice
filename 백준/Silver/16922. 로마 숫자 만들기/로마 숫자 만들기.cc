#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
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
typedef vector<vector<pi>> gra;
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,1,-1 };
int N, M;
int K;
int T;
int res;
int num, num2;
int sum;
string str;
set<int>s;
int arr[4] = { 1,5,10,50 };
void solve(int cnt,int sum,int idx)
{
	if (cnt == N)
	{
		s.insert(sum);
		return;
	}
	for (int i = idx; i < 4; i++)
	{
		solve(cnt + 1, sum + arr[i],i);
	}
	return;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	solve(0,0,0);
	cout << s.size();
}






