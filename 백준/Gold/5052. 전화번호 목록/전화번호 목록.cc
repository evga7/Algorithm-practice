#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000009
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vpi;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef vector<vector<pi>> gra;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int res;
int num, num2;
int T;
int S;
vec v;
struct Node {
	Node* child[10];
	bool finish;
	Node() 
	{
		memset(child, 0, sizeof(child));
		finish = false;
	}
	~Node()
	{
		int i;
		for (i = 0; i < 10; i++)
		{
			if (child[i])
				delete child[i];
		}
	}
	void insret(const char* key)
	{
		if (*key == '\0')
		{
			finish = true;
		}
		else
		{
			int cur = *key - '0';
			if (child[cur] == NULL)
			{
				child[cur] = new Node();
			}
			child[cur]->insret(key + 1);
		}
	}

	bool find(const char* key)
	{
		if (*key == '\0')return false;
		if (finish)return true;
		int cur = *key-'0';
		return child[cur]->find(key + 1);
	}
};

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> T;
	
	while (T--)
	{
		cin >> N;
		Node t;
		int flag = 0;
		char str[10001][11];
		for (i = 0; i < N; i++)
		{
			cin >> str[i];
			t.insret(str[i]);
		}
		for (i = 0; i < N; i++)
		{
			if (t.find(str[i]))
				flag = 1;
		}
		if (flag)cout << "NO\n";
		else cout << "YES\n";
	}
	
}
