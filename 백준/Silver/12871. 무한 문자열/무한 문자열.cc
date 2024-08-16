#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000009
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
int N, M, T, C,K;
ll res;
int num;
int dp[1001][1001];
vec v;
string S, S2;
bool is_inside(int x, int y, int N, int M)
{
	return 0 <= x && x < N && 0 <= y && y < M;
}
int gcd(int a, int b)
{
	while (a != 0)
	{
		int temp = a;
		a = b % a;
		b = temp;
	}
	return b;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> S >> S2;
	int idx = 0;
	int g = gcd(S.length(), S2.length());
	int l = (S.length() * S2.length()) / g;
	string temp = "";
	string temp2 = "";
	for (int i = 0; i < l/ S.length(); i++)
	{
		temp += S;
	}
	for (int i = 0; i < l/ S2.length() ; i++)
	{
		temp2 += S2;
	}
	if (temp == temp2)
		cout << 1;
	else
		cout << 0;
}


