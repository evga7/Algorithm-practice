#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int solution(string name) {
   int answer = 0;
   int len = name.size();
   int i, j;
   string str;
   for (i = 0; i < len; i++)
      str += 'A';
   int answer2;
   answer += min(name.at(0) - 'A', 'Z' - name.at(0) + 1);
   str[0] = name[0];
   int idx = 0;
   int left, right;
   int cnt, cnt2;
   
   while (1)
   {
      int chk = 1;
      cnt = cnt2 = 0;
      for (i=0;i<len;i++)
         if (str[i] != name[i])
         {
            chk = 0;
            break;
         }
      if (chk) break;
      left = right = idx;
      if (right == len)
         right = -1;
      if (left < 0)
         left = len;
      while (1)
      {
         left--;
         cnt++;
         if (left < 0)
            left = len - 1;
         if (str[left] != name[left])
            break;
      }
      while (1)
      {
         right++;
         cnt2++;
         if (right == len )
            right = 0;
         if (str[right] != name[right])
            break;
      }
      if (cnt >= cnt2)
      {
         idx = right;
         str[right] = name[right];
         answer+= min(name[right] - 'A', 'Z' - name[right] + 1);
         answer += cnt2;
      }
      else
      {
         idx = left;
         str[left] = name[left];
         answer += min(name[left] - 'A', 'Z' - name[left] + 1);
         answer += cnt;

      }
   }
   return answer;
}