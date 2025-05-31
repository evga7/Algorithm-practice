#include <bits/stdc++.h>
#define MAX 2147483647
#define MIN -2147483,648
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vpi;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int num;
int res;
int K;
string str;
stack<char>s;
bool is_inside(int x, int y)
{
	if (x >= N || x < 0 || y < 0 || y >= M)return false;
	return true;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> K;
	cin >> str;
	int cnt = 0;
	for (i=0;i<N;i++)
	{
		char temp = str[i];
		while (!s.empty()&&K&&s.top()<temp)
		{
			s.pop();
			K--;
		}
		s.push(temp);
	}
	while (K--)
	{
		s.pop();
	}
	str = "";
	while (!s.empty())
		str+=s.top(), s.pop();
	reverse(str.begin(), str.end());
	cout << str;
}
