#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
int N, M;
int num;
int i, j;
vector<int>v;
int main()
{
	ios::sync_with_stdio(false), cin.tie(NULL);
	cin >> N;
	for (i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}
	sort(v.begin(), v.end());
	int sum = v[0];
	if (sum > 1)
	{
		cout << 1;
		return 0;
	}
	for (i = 1; i < N; i++)
	{
		if (sum + 1 <v[i])
		{
			break;
		}
		sum += v[i];
	}
	cout << sum+1;
}