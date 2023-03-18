#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
map<ll, ll>m;
ll find(ll x)
{
	if (m[x] == 0)
		return x;
	return m[x] = find(m[x]);
}
vector<long long> solution(long long k, vector<long long> room_number) {
	vector<long long> answer;
	int i;
	for (auto num:room_number)
	{
		ll temp= find(num);
		answer.push_back(temp);
		m[temp] = temp + 1;
	}
	return answer;
}