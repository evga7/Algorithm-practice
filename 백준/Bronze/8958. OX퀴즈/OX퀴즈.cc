#include <bits/stdc++.h>
#include <unordered_map>
#define MAX 987654321
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };
int N, M;
int num;
int res = 0;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;

	while (N--)
	{
		int arr[81] = { 0,0 };
		string str;
		cin >> str;
		res = 0;
		for (int i = 0; i < str.size(); i++)
		{
			if (str[i] == 'O')
			{
				if (i == 0)
					arr[i] = 1;
				else
					arr[i] = arr[i - 1] + 1;
				res += arr[i];
			}
			else
				arr[i] = 0;
		}
		cout << res << "\n";
	}
}