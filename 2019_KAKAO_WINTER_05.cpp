#include <bits/stdc++.h>
using namespace std;
bool chk(vector<int>& stones, int k, int mid)
{
	int i;
	int cnt = 0;
	for (i = 0; i < stones.size(); i++)
	{
		if (stones[i] <=mid)
		{
			cnt++;
			if (cnt >=k)
				return false;
		}
		else
            cnt = 0;
	}
	return true;
}
int solution(vector<int> stones, int k) {
	int answer = 0;
	vector<int>v;
	int i;
	int left = 0;
	int right = 200000001;
	answer = right;
	while (left <=right)
	{
		int mid = left + right >> 1;
		if (chk(stones, k, mid))
		{
			left = mid+1;
		}
		else
			right = mid-1;
	}
	return left;
}