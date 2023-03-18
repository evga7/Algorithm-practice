#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    string answer = "";
    int arr[12] = { 31,29,31,30,31,30,31,31,30,31,30,31 };
    string s[7] = {"FRI","SAT", "SUN","MON","TUE","WED","THU" };
    int i;
    int day = 0;
    for (i = 0; i < a-1; i++)
    {
        day += arr[i];
    }
    day += (b-1);
    day %=7;
    answer += s[day];
    return answer;
}
