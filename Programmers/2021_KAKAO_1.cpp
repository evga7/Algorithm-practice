#include <bits/stdc++.h>
#define MAX 1000000001
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, pair<int, int>> pi2;
int dx[4] = {0, -1, 0, 1};
int dy[4] = {-1, 0, 1, 0};
int N, M;
int res;
vector<int> v;
std::string ReplaceAll(std::string &str, const std::string &from, const std::string &to)
{
    size_t start_pos = 0;
    while ((start_pos = str.find(from, start_pos)) != std::string::npos)
    {
        str.replace(start_pos, from.length(), to);
        //start_pos += to.length();
    }
    return str;
}
bool remove_char(char a)
{
    if (isalpha(a) || isdigit(a) || a == '-' ||a=='_'|| a == '.')
        return false;
    return true;
}
string solution(string new_id)
{
    string answer = "";
    for (auto &a : new_id)
    {
        a = tolower(a);
    }
    new_id.erase(remove_if(new_id.begin(),new_id.end(),remove_char),new_id.end());
    ReplaceAll(new_id, "..", ".");
    while(1)
    {
        if (new_id[0]=='.'||new_id[new_id.length()-1]=='.')
        {
            if (new_id[0]=='.')
                new_id.erase(new_id.begin());
            else
            new_id.erase(new_id.end()-1);
        }
        else
        break;
        
    }
    if (new_id.empty())
    {
        new_id=new_id+'a';
    }
    while(new_id.length()>=16)
    {
        new_id.erase(new_id.begin()+15,new_id.end());
    }
    if (new_id[new_id.length()-1]=='.')
        new_id.erase(new_id.end()-1);
    
    while (new_id.length()<=2)
    {
        char temp=new_id[new_id.length()-1];
        new_id=new_id+temp;
    }
    return new_id;
}
