	#include <bits/stdc++.h>
	#include<unordered_map>
	#define MAX 987654321
	#define MIN -987654321
	#define MOD  1000000009
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
	ll N, M, T;
	ll num;
	string str;
	int res = 0;
	vector<ll>v;
	priority_queue<pii, vector<pii>, greater<pii>>pq;
	int main()
	{
		ios::sync_with_stdio(false);
		cin.tie(0);
		cout.tie(0);
		cin >> N;
		while (N--)
		{
			cin >> num;
			if (num)
			{
				pq.push({ abs(num),num });
			}
			else
			{
				if (pq.empty())
				{
					cout << "0\n";
					continue;
				}
				cout << pq.top().second << "\n";
				pq.pop();
			}
		}
	}





