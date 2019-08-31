#include <iostream>
#include <string>
#include <vector>
using namespace std;
int DFS(vector<int> numbers,int sum, int target,int cnt,int index)
{

	if (cnt == numbers.size())
	{
		if (sum == target)
		{
			return 1;
		}
		return 0;
	}
	return DFS(numbers,sum +numbers[index], target, cnt+1,index+1) + DFS(numbers,sum - numbers[index], target, cnt + 1,index+1);
}

int solution(vector<int> numbers, int target) {
    return DFS(numbers,0,target,0,0);
}