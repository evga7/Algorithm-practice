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
int res = MAX;
int num, num2;
string str;
int arr[11][11];
int paper[6] = { 0,5,5,5,5,5 };
int f;
void sol(int x, int y, int size, int op)
{
	int i, j;
	for (i = x; i < x + size; i++)
		for (j = y; j < y + size; j++)
			arr[i][j] = op;
}
bool chk(int x, int y, int size)
{
	int i, j;
	if (x + size > 10 || y + size > 10)return false;
	for (i = x; i < x + size; i++)
	{
		for (j = y; j < y + size; j++)
		{
			if (!arr[i][j]) return false;
		}
	}
	return true;
}
void solve(int x, int y, int cnt)
{
	if (cnt >= res)return;
	if (y == 10)
	{
		solve(x + 1, 0, cnt);
		return;
	}
	if (x == 10)
	{
		res = min(res, cnt);
		return;
	}
	if (!arr[x][y])
	{
		solve(x, y + 1, cnt);
		return;
	}
	int i, j;
	for (i = 5; i >= 1; i--)
	{
		if (!paper[i])continue;
		if (chk(x, y, i))
		{
			paper[i]--;
			sol(x, y, i, 0);
			solve(x, y + i, cnt + 1);
			sol(x, y, i, 1);
			paper[i]++;
		}
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	for (i = 0; i < 10; i++)
		for (j = 0; j < 10; j++)
			cin >> arr[i][j];
	solve(0, 0, 0);
	if (res == MAX)res = -1;
	cout << res;
}