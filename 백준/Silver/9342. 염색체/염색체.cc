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
bool is_inside(int x, int y)
{
    return 0 <= x && x < N && 0 <= y && y < M;
}
bool chk(string s)
{
    if (!('A' <= s[0] && s[0] <= 'F'))
        return false;
    int idx = 1;
    while (idx < s.length() && s[idx] == 'A')
        idx += 1;
    if (idx==s.length())return false;
    while (idx < s.length() && s[idx] == 'F')
        idx += 1;
    if (idx == s.length())return false;
    while (idx < s.length() && s[idx] == 'C')
        idx += 1;
    vector<char>v;
    while (idx < s.length())
    {
        v.push_back(s[idx++]);
        if (v.size() > 1)return false;
    }
    if (v.size()==0 ||('A' <= v[0] && v[0] <= 'F'))return true;
    return false;
    
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    while (T)
    {
        T -= 1;
        cin >> s;
        if (chk(s))
            cout << "Infected!\n";
        else
            cout << "Good\n";
    }


}
