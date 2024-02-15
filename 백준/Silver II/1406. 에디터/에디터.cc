#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
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
int dx[4] = { 0, 0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int N, M, T;
int S;
ll res;
int num, num2;
typedef struct Node
{
	char c;
	Node* next;
	Node* prev;

}Node;
Node* newNode(int c)
{
	Node* New;
	New = (Node*)malloc(sizeof(Node));
	New->c = c;
	New->next = NULL;
	New->prev = NULL;
	return New;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	string s;
	cin >> s;
	Node* head = newNode('.');
	Node *p = head;
	for (auto cur : s)
	{
		auto curNode = newNode(cur);
		p->next = curNode;
		curNode->prev = p;
		p = p->next;
	}
	auto t= newNode('.');
	p->next = t;
	t->prev = p;
	p = p->next;
	cin >> M;
	for (int i = 0; i < M; i++)
	{
		char op;
		cin >> op;
		if (op == 'P')
		{
			char cc;
			cin >> cc;
			auto curNode = newNode(cc);
			p->prev->next = curNode;
			curNode->prev = p->prev;
			curNode->next = p;
			p->prev = curNode;
			
		}
		else if (op == 'L')
		{
			if (p->prev->c != '.')
				p = p->prev;
		}
		else if (op == 'D')
		{
			if (p->c != '.')
			{
				p = p->next;
			}
		}
		else if (op == 'B')
		{
			if (p->prev->c != '.')
			{
				Node* temp = p->prev;
				p->prev = temp->prev;
				p->prev->next = p;
				delete temp;
			}

		}
	}
	while (1)
	{
		head = head->next;
		if (head->next == NULL)break;
		cout << head->c;
	}
}