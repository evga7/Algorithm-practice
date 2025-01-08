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
int res;
int num, num2;
string f;
string str;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> T;
	cin.ignore();
	while (T--)
	{
		vector<string>v;
		set<string>s;
		getline(cin, f);
		string temp = "";
		for (auto cur : f)
		{
			if (cur == ' ')
			{
				v.push_back(temp);
				temp.clear(); continue;
			}
			else
			{
				temp.push_back(cur);
			}
		}
		if (!temp.empty())
			v.push_back(temp);
		while (1)
		{
			getline(cin, str);
			if (str == "what does the fox say?") break;
			else
			{
				auto idx = str.find_last_of(' ');
				temp = str.substr(idx + 1, str.size() - idx);
				s.insert(temp);
			}
		}
		for (auto cur : v)
		{
			if (s.find(cur) == s.end())
				cout << cur << " ";
		}
		cout << "\n";
	}
}