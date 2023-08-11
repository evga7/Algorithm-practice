#include <bits/stdc++.h>
using namespace std;
int parent[201];
int find(int x){
    if (x==parent[x])
        return x;
    return parent[x]=find(parent[x]);
}
int uni(int x,int y)
{
    x=find(x);
    y=find(y);
    if (x!=y)
    {
        parent[y]=x;
        return true;
    }
    return false;
}
int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for (int i=1;i<n;i++)
        parent[i]=i;
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<n;j++)
        {
            if (computers[i][j] && i!=j)
            {
                if (uni(i,j))answer+=1;
            }
        }
    }
    return n-answer;
}