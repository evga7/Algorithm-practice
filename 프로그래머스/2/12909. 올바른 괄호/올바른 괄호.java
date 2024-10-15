import java.util.*;
class Solution {
    boolean solution(String s) {
        Stack<Character> st= new Stack<>();
        for (char c:s.toCharArray())
        {
            if (c=='(')
                st.push(c);
            else
            {
                if (st.empty())
                    return false;
                char t=st.pop();
            }
        }
        if (st.empty())
            return true;
        return false;
    }
}