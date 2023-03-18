#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int N;
bool comp(const string &v, string &v2)
{
    if (v[N]!=v2[N])
        return v[N]<v2[N];
	else return v<v2;
	

}
vector<string> solution(vector<string> strings, int n) {
	vector<string> answer;
	N = n;
	sort(strings.begin(), strings.end(), comp);
	answer = strings;
	return answer;
}