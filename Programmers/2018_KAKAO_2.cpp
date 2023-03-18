#include <string>
#include <vector>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    int i,j;
    for (i=0;i<n;i++)
    {
        int num=arr1[i]|arr2[i];
        string temp="";
        for (j=0;j<n;j++)
        {
            if (num%2==1)
                temp='#'+temp;
            else
                temp=' '+temp;
            num=num>>1;
        }
        answer.push_back(temp);
    }
    return answer;
}