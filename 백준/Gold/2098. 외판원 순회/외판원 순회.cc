#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000000
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
int dx[4] = { 0,1,0,-1 };//왼 아 오 위
int dy[4] = { -1,0,1,0 };
int N, M, T;
int num;
int V, E, K;
string s;
int res=987654321;
int arr[16][16];
int dp[1 << 16][16];
bool is_inside(int x, int y)
{
    return 0 <= x && x < N && 0 <= y && y < M;
}
int go(int bit,int cur,int start)
{
    if (bit == (1 << N) - 1)
    {
        if (cur == start)
        {
            return 0;
        }
        return 987654321;
    }
    int& ret = dp[bit][cur];
    if (ret != -1)
        return ret;
    ret = 987654321;
    for (int i = 0; i < N; i++)
    {
        if (arr[cur][i] && !(bit & (1 << i)))
        {
            ret=min(ret,go(bit | (1 << i), i,start) + arr[cur][i]);
        }
    }
    return ret;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        for (int j=0;j<N;j++)
        {
            cin >> arr[i][j];
        }
    }
    memset(dp, -1, sizeof(dp));
    cout << go(0, 0, 0);


}
