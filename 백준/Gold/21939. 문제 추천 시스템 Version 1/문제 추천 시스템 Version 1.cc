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
int level;
int V, E, K;
int bx, by;
int rx, ry;
bool is_inside(int x, int y)
{
    return 0 <= x && x < N && 0 <= y && y < M;
}
map<int, int>m;
typedef struct info {
    int num, level;
}info;
typedef struct info2 {
    int num, level;
}info2;
struct cmp {
    bool operator()(const info& v1, const info& v2)
    {
        if (v1.level == v2.level)
            return v1.num > v2.num;
        return v1.level > v2.level;
    }
};
struct cmp2 {
    bool operator()(const info2& v1, const info2& v2)
    {
        if (v1.level == v2.level)
            return v1.num < v2.num;
        return v1.level < v2.level;
    }
};
priority_queue<info, vector<info>, cmp>min_pq;
priority_queue<info2,vector<info2>,cmp2>max_pq;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    int a, b;
    for (int i = 0; i < N; ++i)
    {
        cin >> a >> b;
        min_pq.push({ a,b });
        max_pq.push({ a,b });
        m[a] = b;
    }
    cin >> M;
    for (int i = 0; i < M; i++)
    {
        string op;
        cin >> op;
        if (op == "add")
        {
            cin >> num >> level;
            min_pq.push({ num,level });
            max_pq.push({ num,level });
            m[num] = level;
        }
        else if (op == "recommend")
        {
            cin >> num;

            if (num == 1)
            {
                while (m.find(max_pq.top().num) == m.end()|| max_pq.top().level != m[max_pq.top().num])
                    max_pq.pop();
                cout << max_pq.top().num;
            }
            else
            {
                while (m.find(min_pq.top().num) == m.end()|| min_pq.top().level != m[min_pq.top().num])
                    min_pq.pop();
                cout << min_pq.top().num;
            }
            cout << "\n";
        }
        else {
            cin >> num;
            m.erase(num);
        }
    }

}
