#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
string conv(int a, int b)
{
	string res = "";
	while (a)
	{
		res.push_back(a % b + 48);
		a /= b;
	}
	reverse(res.begin(), res.end());
	return res;
}
int prime_chk(ll num2)
{
	if (num2 == 1)return 0;
	for (ll i = 2; i <= sqrt(num2); i++)
	{
		if (!(num2%i))
			return 0;
	}
	return 1;
}
int solution(int n, int k) {
	int answer = 0;
	string temp;
	temp = to_string(n);
	if (k<10)
		temp = conv(n, k);
	string str = "";
	ll num;
	for (auto cur : temp)
	{
		if (cur != '0')
		{
			str.push_back(cur);
		}
		else
		{
			if (!str.empty())
			{
				num = stoll(str);
				if (prime_chk(num))
				{
						answer++;
				}
				str.clear();
			}
		}
	}
	if (!str.empty())
	{
		num = stoll(str);
		if (prime_chk(num))
		{
			answer++;
		}
	}
	return answer;
}