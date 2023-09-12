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
ll N, M, T;
int L;
int num;
int V, E, K;
vec v;
int sx, sy;
bool is_inside(int x, int y)
{
    return 0 <= x && x < N && 0 <= y && y < M;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    vec v;
    for (int i = 0; i < N; ++i)
    {
        cin >> num;
        v.push_back(num);
    }
    bool f=false;
    for (int i = 0; i < N; i++)
    {
        M -= v[i];
        if (M < 0)
        {
            cout << i + 1;
            f=true;
            break;
        }

    }
    if (!f)
    {
        for (int i = N - 1; i >= 0; i--)
        {
            M -= v[i];
            if (M < 0)
            {
                cout << i + 1;
                break;
            }
            
        }
    }

}
