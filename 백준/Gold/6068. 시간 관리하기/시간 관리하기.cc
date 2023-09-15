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
vector<pair<int, int>>v;
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
        v.push_back({ b,a });
    }
    sort(v.begin(), v.end());
    int left = 0;
    int right = 1000000000;
    while (left <= right)
    {
        int mid = left + right >> 1;
        int start = mid;
        bool flag = true;
        for (auto cur : v)
        {
            int cost = cur.second;
            int m_time = cur.first;
            if (start + cost > m_time)
            {
                flag = false;
                break;
            }
            start += cost;
        }
        if (flag)
            left = mid + 1;
        else
            right = mid - 1;
    }
    cout<<left-1;
}
