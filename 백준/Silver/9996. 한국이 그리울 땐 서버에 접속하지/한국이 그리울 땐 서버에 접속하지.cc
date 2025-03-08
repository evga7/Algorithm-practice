#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000009
#define pb push_back
#define pob pop_back
#define ms memset
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
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int T;
int K;
int res;
int num, num2;
string A;
string B;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	cin >> A;
	string front;
	string back;
	int flag = 0;
	for (i = 0; i < A.size(); i++)
	{
		if (A[i] == '*')
		{
			flag = 1;
			continue;
		}
		if (!flag)
			front.push_back(A[i]);
		else
			back.push_back(A[i]);
}
	for (i = 0; i < N; i++)
	{
		cin >> B;
		flag = 0;
		if (front.size() + back.size() > B.size())
			flag = 1;
		else if (B.substr(0, front.size()) != front)
			flag = 1;
		else if (B.substr(B.size() - back.size(), back.size()) != back)
			flag = 1;
		if (!flag)
			cout << "DA\n";
		else
			cout << "NE\n";
	}

}





