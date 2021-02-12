#include<bits/stdc++.h>
using namespace std;
int parent[101];
bool cmp(vector<int> &v1,vector<int> &v2)
{
    return v1[2]<v2[2];
}
int find(int x)
{
    if(parent[x]==x)
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
int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    int i;
    for(i=1;i<=n;i++)
        parent[i]=i;
    sort(costs.begin(),costs.end(),cmp);
    for (i=0;i<costs.size();i++)
    {
        if (uni(costs[i][0],costs[i][1]))
            answer+=costs[i][2];
    }
    return answer;
}    
