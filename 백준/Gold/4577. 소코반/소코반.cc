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
char arr[15][15];
map<char, int>m;
set<pair<int, int>>st;
void go(int& x, int& y, int op)
{
    int n_x = x + dx[op];
    int n_y = y + dy[op];
    char& nxt = arr[n_x][n_y];
    if (!is_inside(n_x, n_y) || nxt == '#')
        return;
    if (nxt == '.')
    {
        arr[x][y] = '.';
        x = n_x, y = n_y;
        nxt = 'w';
    }
    else if (nxt == 'b')
    {
        int n_x2 = n_x + dx[op];
        int n_y2 = n_y + dy[op];
        if (is_inside(n_x2, n_y2) && arr[n_x2][n_y2] != '#' && arr[n_x2][n_y2] != 'b')
        {
            nxt = 'w';
            arr[n_x2][n_y2] = 'b';
            arr[x][y] = '.';
            x = n_x, y = n_y;
        }
    }

}
bool chk()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (arr[i][j] == 'b' && st.find({i,j})==st.end())
                return false;
        }
    }
    return true;
}
void p(bool pp)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (pp)
            {
                cout << arr[i][j];
                continue;
            }
            if (st.find({ i,j }) != st.end())
            {
                if (arr[i][j] == 'w')
                    arr[i][j] = 'W';
                else if (arr[i][j] == 'b')
                    arr[i][j] = 'B';
                else if (arr[i][j] == '.')
                    arr[i][j] = '+';
            }
        }
        if (pp)
            cout << "\n";
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    m['U'] = 3;
    m['L'] = 0;
    m['R'] = 2;
    m['D'] = 1;
    int idx = 0;
    while (true)
    {
        cin >> N >> M;
        if (N == 0 && M == 0)break;
        st.clear();
        idx += 1;
        int x, y;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                cin >> arr[i][j];
                if (arr[i][j] == 'W'||arr[i][j]=='B'||arr[i][j]=='+')
                {
                    st.insert({ i,j });
                    char& nxt = arr[i][j];
                    if (nxt == 'W')
                        nxt = 'w';
                    else if (nxt == 'B')
                        nxt = 'b';
                    else
                        nxt = '.';
                }
                if (arr[i][j] == 'w')
                {
                    x = i, y = j;
                }
            }
        }
        cin >> s;
        for (auto cur : s)
        {
            int op = m[cur];
            go(x, y, op);
            if (chk())break;
        }
        cout << "Game " << idx << ": ";
        p(0);
        if (chk())
            cout << "complete\n";
        else
            cout << "incomplete\n";
        p(1);
    }
}

