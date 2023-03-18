#include <string>
#include <vector>

using namespace std;

bool solution(vector<string> phone_book) {
	bool answer = true;
	int i, j,k;
	for (i = 0; i < phone_book.size(); i++)
	{
		string temp = phone_book[i];
		for (j = 0; j <phone_book.size(); j++)
		{
            if (i==j)
                continue;
			int flag = 0;
			for (k = 0; k < temp.size(); k++)
			{
				if (temp[k] != phone_book[j][k])
				{
					flag = 1;
                    break;
				}
				
			}
			if (!flag)
				return 0;
		}
	}
	return answer;
}