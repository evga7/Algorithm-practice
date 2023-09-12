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
int arr[6][3];
typedef struct info {
    int x, y;
}info;
vector<info>vs;
bool is_inside(int x, int y)
{
    return 0 <= x && x < N && 0 <= y && y < M;
}
bool flag = false;

bool chk()
{
    for (int i = 0; i < 6; i++)
    {
        if (arr[i][0] || arr[i][1] || arr[i][2])return false;
    }
    return true;
}
void go(int idx)
{
    if (flag)return;
    if (idx==15)
    {
        if (chk())
            flag = true;
        return;
    }
    int t1, t2;
    t1 = vs[idx].x;
    t2 = vs[idx].y;
    if (arr[t1][0] && arr[t2][2])
    {
        arr[t1][0] -= 1;
        arr[t2][2] -= 1;
        go(idx + 1);
        arr[t1][0] += 1;
        arr[t2][2] += 1;

    }
    if (arr[t1][1] && arr[t2][1])
    {
        arr[t1][1] -= 1;
        arr[t2][1] -= 1;
        go(idx + 1);
        arr[t1][1] += 1;
        arr[t2][1] += 1;
    }
    if (arr[t1][2] && arr[t2][0])
    {
        arr[t1][2] -= 1;
        arr[t2][0] -= 1;
        go(idx + 1);
        arr[t1][2] += 1;
        arr[t2][0] += 1;

    }

}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int idx = 0;
    while (idx < 4)
    {
        int wl, d;
        flag = false;
        idx += 1;
        for (int i = 0; i < 6; i++)
        {
            int win, draw, lose;

            cin >> win >> draw >> lose;
            arr[i][0] = win;
            arr[i][1] = draw;
            arr[i][2] = lose;
        }
        for (int i = 0; i < 6; i++)
        {
            for (int j = i + 1; j < 6; j++)
            {
                vs.push_back({i,j});
            }
        }
        go(0);
        if (flag)
            cout << 1;
        else
            cout << 0;
        cout << "\n";
    }


}
