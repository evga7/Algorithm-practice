#include <string>
#include <vector>

using namespace std;

int GCD(int a, int b)
{
	int temp;
	while (b != 0)
	{
		temp = b;
		b = a % b;
		a = temp;
	}
	return a;
}
int solution(vector<int> arr) {
	int answer = 0;
	int i, num;
	num = arr[0];
	int num2=arr[0];
	for (i=0;i<arr.size()-1;i++)
	{
		num = GCD(num2, arr[i + 1]);
		num2 = (num2*arr[i + 1]) / num;
	}
    answer=num2;
	return answer;
}