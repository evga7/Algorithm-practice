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
bool is_inside(int x, int y)
{
    return 0 <= x && x < N && 0 <= y && y < M;
}
int V, E, K;
string s;
int res;
int arr[101][101];
void go(int sx, int sy, int x_size, int y_size)
{
    for (int i = sx; i < min(sx + x_size, 101); i++)
    {
        for (int j = sy; j < min(sy + y_size,101); j++)
        {
            if (!arr[i][j])return;
        }
    }
    res = max(res, x_size * y_size);
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    int a, b;
    for (int i = 0; i < N; i++)
    {
        cin >> a >> b;
        for (int j = a; j <min(a + 10, 101); j++)
        {
            for (int k = b; k <min(b + 10, 101); k++)
            {
                arr[j][k] = 1;
            }
        }
    }
    for (int i = 1; i <=100; i++)
    {
        for (int j = 1; j <=100; j++)
        {
            for (int k = 1; k <=101-i; k++)
            {
                for (int l = 1; l <=101-j; l++)
                {
                    go(i, j, k, l);
                }
            }
        }
    }
    cout << res;
    
}

