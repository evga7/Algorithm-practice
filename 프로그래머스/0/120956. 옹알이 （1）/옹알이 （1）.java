class Solution {
    static String c[]={"aya","ye","woo","ma"};
    static boolean go(String s)
    {
        for (int i=0;i<4;i++)
            s=s.replaceAll(c[i]," ");
        s=s.replaceAll(" ","");
        if (s.length()==0)
            return true;
        return false;
    }
    public int solution(String[] babbling) {
        int answer = 0;
        for (int i=0;i<babbling.length;i++)
        {
            if (go(babbling[i])==true)
                answer+=1;
        }
        return answer;
    }
}