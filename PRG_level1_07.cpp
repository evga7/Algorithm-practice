#include <vector>
#include <iostream>

using namespace std;
vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    int i;
    for (i=0;i<arr.size();i++)
    {
		if (i == 0)
		{
			answer.push_back(arr[i]);
		}
		else if (arr[i] != answer.back())
		{
			answer.push_back(arr[i]);
		}
	
    }
    return answer;
}