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
int L;
int num;
int V, E, K;
bool is_inside(int x, int y)
{
    return 0 <= x && x < N && 0 <= y && y < M;
}
int arr[65][65];
int dp[65][65][101];
int go(int x, int y,int jump)
{
    if (x == N - 1 && y == N - 1)
        return 1;
    int& ret = dp[x][y][jump];
    if (ret != -1)
        return ret;
    ret = 0;
    int cnt = arr[x][y];
    if (x + cnt < N)
        ret = max(ret, go(x + cnt, y, cnt));
    if (y + cnt < N)
        ret = max(ret, go(x, y+cnt, cnt));
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
        for (int j = 0; j < N; j++)
        {
            cin >> arr[i][j];
        }
    }
    memset(dp, -1, sizeof(dp));
    int res = go(0, 0, 0);
    if (res)
        cout << "HaruHaru";
    else
        cout << "Hing";


}
