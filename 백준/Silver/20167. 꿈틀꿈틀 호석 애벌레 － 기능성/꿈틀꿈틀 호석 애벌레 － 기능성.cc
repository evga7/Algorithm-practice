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
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
int dx[4] = { 1,-1,0,0 };
int dy[4] = { 0,0,1,-1 };
int N, M, T;
int L;
int num;
int V, E, K;
string str;
int res;
vec v;
void solve(int idx,int sum,int score)
{
	if (sum >= M)
	{
		score += sum - M;
		sum = 0;
	}
	if (idx == N)
	{
		res = max(res, score);
		return;
	}
	solve(idx + 1, sum + v[idx], score);
	solve(idx + 1, 0, score);

}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	for (i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}
	solve(0,0,0);
	cout << res;
}





