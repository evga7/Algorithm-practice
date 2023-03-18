#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int solution(vector<int> citations) {
	int answer = 0;
	int i;
	sort(citations.begin(), citations.end());
	int mid = 0;
	for (i = 0; i < citations.size(); i++)
		mid += citations[i];
	mid /= citations.size();
	int num = 1;
	while (1)
	{
		if (num >mid)
			break;
		int low, high;
		low = high = 0;
		for (i = 0; i < citations.size(); i++)
		{
			if (citations[i] >= num) high++;
			if (citations[i] <= num) low++;
		}
		if (high >= num && low <= num)
			answer = num;
		num++;
	}
	cout << answer;
	return answer;
}