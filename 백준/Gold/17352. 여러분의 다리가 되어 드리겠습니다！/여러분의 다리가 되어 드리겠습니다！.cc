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
typedef vector<vector<pi>> gra;
//int dx[4] = { 0,0,-1,1 };
//int dy[4] = { 1,-1,0,0 };
const int dy[9] = { -1,0,1,1,1,0,-1,-1,0 };
const int dx[9] = { 1,1,1,0,-1,-1,-1,0,0 };
int N, M;
int T;
int K;
int res;
int num, num2;
string str;
int parent[3000001];
int find(int x)
{
	if (parent[x] == x)return x;
	return parent[x] = find(parent[x]);
}
bool uni(int x, int y)
{
	x = find(x);
	y = find(y);
	if (x != y)
	{
		parent[y] = x;
		return true;
	}
	return false;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	for (i = 1; i <= N; i++)
		parent[i] = i;
	for (i = 0; i < N - 2; i++)
	{
		cin >> num >> num2;
		uni(num, num2);
	}
	num = find(num2);
	if (!num)num = 1;
	for (i = 1; i <= N; i++)
	{
		if (uni(num, i))
		{
			cout << num << " " << i;
			break;
		}
	}
}





