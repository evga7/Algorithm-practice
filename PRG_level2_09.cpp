#include <string>
#include <vector>
#include <math.h>
using namespace std;

vector<int> solution(int brown, int red) {
    vector<int> answer;
    int i;
    int len=brown+red;
    
    for(i=3;i<=sqrt(len);i++)
    {
        if (len%i==0)
        {
            if((len/i-2)*(i-2)==red)
            {
                answer.push_back(len/i);
                answer.push_back(i);
            }
        }
    }
    return answer;
}