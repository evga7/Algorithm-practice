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
int res;
int dist[101][101];
int st[101][101];
typedef struct info {
    int cost,x;
}info;
bool is_inside(int x, int y)
{
    return 0 <= x && x < N && 0 <= y && y < M;
}
void go(int start, int end)
{
    int cur = start;
    deque<int>dq;
    dq.push_back(start);
    while (cur!=end)
    {
        cur = st[cur][end];
        if (cur == 0)break;
        dq.push_back(cur);
    }
    cout << dq.size() << " ";
    for (auto cur : dq)
        cout << cur << " ";
    cout << "\n";
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    int a, b, c;
    fill(&dist[0][0],&dist[N][N], 987654321);
    for (int i = 0; i <M; i++)
    {
        cin >> a >> b >> c;
        dist[a][b] = min(dist[a][b], c);
        st[a][b] = b;

    }
    for (int k = 1; k <= N; k++)
    {
        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= N; j++)
            {
                if (i == j)continue;
                if (dist[i][k] + dist[k][j] <dist[i][j])
                {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    st[i][j] = st[i][k];
                }
            }
        }
    }
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            if (dist[i][j] == 987654321)
                dist[i][j] = 0;
            cout << dist[i][j] << " ";
        }
        cout << "\n";
    }
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            if (i == j||dist[i][j]==0)
            {
                cout << "0\n";
                continue;
            }
            go(i, j);
        }
    }

}
