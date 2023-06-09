#include <string>
#include <vector>
using namespace std;
#define MAX 987654321
int res=MAX;
int n;
int num;
void solve(int sum,int cnt)
{
    int i;
    if (res<=cnt||cnt>8)
        return;
    if (sum==num)
        res=min(cnt,res);
    int temp=0;
    for (i=cnt;i<8;i++)
    {
        temp=temp*10+n;
        solve(sum+temp,i+1);
        solve(sum-temp,i+1);
        solve(sum/temp,i+1);
        solve(sum*temp,i+1);
    }
}
int solution(int N, int number) {
    int answer = 0;
    n=N;
    num=number;
    solve(0,0);
    if (res==MAX)
        res=-1;
    return res;
}