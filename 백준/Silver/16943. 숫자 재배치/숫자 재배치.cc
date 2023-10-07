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
ll num, num2;
int sum;
string str;
string str2;
bool cmp(char& c1, char& c2)
{
	return c1 > c2;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> str >> str2;
	int t2 = stoi(str2);
	sort(str.begin(), str.end(),cmp);
	int s = str.size();
	do
	{
		int temp = stoi(str);
		string temp2 = to_string(temp);
		if (temp2.size() < s)continue;
		if (temp <=t2)
		{
			res = temp;
			break;
		}

	} while (prev_permutation(str.begin(), str.end()));
	if (!res)
		cout << -1;
	else
		cout << res;
}






