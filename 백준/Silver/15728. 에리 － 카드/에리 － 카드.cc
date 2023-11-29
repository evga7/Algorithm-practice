#include <bits/stdc++.h>
#define MIN -987654321
using namespace std;
typedef vector<int> vec;
int N, M;
int res;
int num;
vec v;
vec v2;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j, k;
	cin >> N >> M;
	for (i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}
	for (i = 0; i < N; i++)
	{
		cin >> num;
		v2.push_back(num);
	}
	int t;
	for (k = 0; k <=M; k++)
	{
		res = MIN;
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < N - k; j++)
			{
				if (res < v[i] * v2[j])
				{
					res = v[i] * v2[j];
					t = j;
				}
			}
		}
		if (k < M)
			v2.erase(v2.begin() + t);
	}
	cout << res;
}