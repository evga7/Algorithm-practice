#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
int N;
int is_friends[11][11];

int solve(int chk[11])
{
    int f = -1;
    int i, j;
    int next;
    for (i = 0; i < N; i++)
        if (!chk[i]) {
            f = i;
            break;
        }

    if (f==-1) return 1;
    int ret = 0;
    for (i = f+1; i < N; i++)
    {
        if (is_friends[f][i] && !chk[i])
        {
            chk[i] =chk[f]= true;
            ret += solve(chk);
            chk[i] = chk[f] = false;
        }
    }
    return ret;
}
int main() {
    ios_base::sync_with_stdio(false), cin.tie(0);
    int i, j;
    int T;
    cin >> T;
    int chk[11];
    while (T--)
    {
        int M;
        int a, b;
        cin >> N >> M;

        memset(chk, false,sizeof(chk));
        memset(is_friends, 0,sizeof(is_friends));
        for (i = 0; i < M; i++)
        {
            cin >> a >> b;
            is_friends[a][b]=1;
            is_friends[b][a]=1;
        }
        cout<<solve(chk)<<"\n";
    }
}