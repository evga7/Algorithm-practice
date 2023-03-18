#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;
unordered_map<int,vector<int>>m;
int solution(vector<int> a)
{
	int answer = 0;
	int len = a.size();
	int i, j;
	for (i = 0; i < len; i++)m[a[i]].push_back(i);
	for (auto num : m)
	{
		int len2 = num.second.size();
		int left = -1;
		int cnt = 0;
		if (len2 <= answer)continue;
		for (i = 0; i < len2; i++)
		{
			int idx = num.second[i];
			int back = idx - 1;
			int right = idx + 1;
			if (back >= 0 && left < back&&a[idx]!=a[back])
			{
				left = back;
				cnt++;
			}
			else if (right < len && left < right && a[idx] != a[right])
			{
				left = right;
				cnt++;
			}
		}
		answer = max(cnt, answer);
	}
	return answer * 2;
}