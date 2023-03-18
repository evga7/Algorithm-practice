#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> heights) {
    vector<int> answer;
    int i,j;
    int cnt=0;
    for (i=0;i<heights.size();i++)
    {
        int flag=1;
        cnt=1;
        for (j=i-1;j>=0;j--)
        {
            if (heights[i]<heights[j])
            {
                flag=0;
                answer.push_back(j+1);
                break;
            }
        }
        if (flag)
            answer.push_back(0);
    }
    return answer;
}