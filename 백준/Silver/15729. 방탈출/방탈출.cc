#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
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
int N, M;
int res;
int T;
string str;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	char temp;
	for (i = 0; i < N; i++)
	{
		cin >> temp;
		str.push_back(temp);
	}
	int s = str.size();
	for (i = 0; i < s; i++)
	{
		if (str[i] == '1')
		{
			res++;
			str[i] = '1' - str[i] + '0';
			str[i + 1] = '1' - str[i + 1] + '0';
			str[i + 2] = '1' - str[i + 2] + '0';
		}
	}
	cout << res;
}


