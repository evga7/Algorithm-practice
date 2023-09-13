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
char arr[11][11];
int bx, by;
int rx, ry;
bool visited[11][11][11][11];
typedef struct info {
    int rx, ry, bx, by,cost;
};
struct cmp 
{
    bool operator()(const info& v1, const info& v2)
    {
        return v1.cost > v2.cost;
    }
};
bool is_inside(int x, int y)
{
    return 0 <= x && x < N && 0 <= y && y < M;
}
void chk(int rx, int ry, int bx, int by,int &n_rx, int& n_ry, int& n_bx, int& n_by,int op)
{
    if (op == 0)
    {
        if (ry < by)
            n_by += 1;
        else
            n_ry += 1;
    }
    else if (op == 1)
    {
        if (rx > bx)
            n_bx -= 1;
        else
            n_rx -= 1;
    }
    else if (op == 2)
    {
        if (ry < by)
            n_ry -= 1;
        else
            n_by -= 1;
    }
    else if (op == 3)
    {
        if (rx > bx)
            n_rx += 1;
        else
            n_bx += 1;
    }
}
int go()
{
    priority_queue<info,vector<info>,cmp>pq;
    pq.push({ rx,ry,bx,by,0 });
    while (!pq.empty())
    {
        auto cur = pq.top();
        pq.pop();
        int rx, ry, bx, by,cost;
        rx = cur.rx;
        ry = cur.ry;
        bx = cur.bx;
        by = cur.by;
        cost = cur.cost;
        
        if (arr[rx][ry] == 'O')return cost;
        for (int i = 0; i < 4; i++)
        {
            int n_rx = rx;
            int n_ry = ry;
            int n_bx = bx;
            int n_by = by;
            while (is_inside(n_rx+dx[i],n_ry+dy[i])&&arr[n_rx+dx[i]][n_ry+dy[i]]!='#')
            {
                n_rx += dx[i];
                n_ry += dy[i];
                if (arr[n_rx][n_ry] == 'O')break;
            }
            while (is_inside(n_bx + dx[i], n_by + dy[i]) && arr[n_bx + dx[i]][n_by + dy[i]] != '#')
            {
                n_bx += dx[i];
                n_by += dy[i];
                if (arr[n_bx][n_by] == 'O')break;
            }
            if (arr[n_bx][n_by] == 'O' || cost + 1 > 10)continue;
            if (n_rx == n_bx && n_ry == n_by)
            {
                chk(rx,ry,bx,by,n_rx, n_ry, n_bx, n_by,i);
            }
            if (!visited[n_rx][n_ry][n_bx][n_by])
            {
                visited[n_rx][n_ry][n_bx][n_by] = 1;
                pq.push({ n_rx,n_ry,n_bx,n_by,cost + 1 });
            }
        }

    }


    return -1;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == 'B')
            {
                bx = i, by = j;
            }
            if (arr[i][j] == 'R')
            {
                rx = i, ry = j;
            }
        }
    }
    cout << go();

}
