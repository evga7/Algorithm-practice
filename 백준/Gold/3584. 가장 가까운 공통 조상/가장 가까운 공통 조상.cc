#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX = 100001;
const int MOD = 1e9 + 9;
int l[MAX];
int g[MAX];

int go(int cur) {
    if (cur == 0) {
        return 0;
    }
    if (l[cur] != -1) {
        return l[cur];
    }
    int ret = 0;
    ret = max(ret, go(g[cur]) + 1);
    l[cur] = ret;
    return ret;
}

void solve(int left, int right) {
    while (left != right) {
        if (l[left] > l[right]) {
            left = g[left];
        } else {
            right = g[right];
        }
    }
    cout << left << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    
    while (T--) {
        int N;
        cin >> N;
        
        fill(l, l + N + 1, -1);
        fill(g, g + N + 1, 0);
        
        for (int i = 0; i < N - 1; i++) {
            int A, B;
            cin >> A >> B;
            g[B] = A;
        }
        
        for (int i = 1; i <= N; i++) {
            go(i);
        }
        
        int A, B;
        cin >> A >> B;
        solve(A, B);
    }
    
    return 0;
}
