class Solution {
    public static String solution(String s) {
        String answer = "";
        boolean flag=true;
        for (int i=0;i<s.length();i++)
        {
            char cur = s.charAt(i);
            if (cur==' ')
            {
                answer+=' ';
                flag=true;
                continue;
            }
            if (flag==true)
            {
                if (Character.isLowerCase(cur))
                    answer+=Character.toUpperCase(cur);
                else
                    answer+=cur;
                flag=false;
                continue;
            }
            answer+=Character.toLowerCase(cur);
            
        }
        return answer;
    }
}