import java.util.*;
class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        Arrays.sort(routes, (a,b)-> Integer.compare(a[1], b[1]));
        int pos=-30001;
        for (int i=0;i<routes.length;i++)
        {
            if (pos>=routes[i][0])continue;
            pos=routes[i][1];
            answer+=1;
        }
        
        return answer;
    }
}