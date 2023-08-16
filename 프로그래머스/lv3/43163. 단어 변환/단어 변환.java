class Solution {
    static int []visited=new int[51];
    static String t;
    static int res=987654321;
    static String[] w;
    public boolean chk(String s,String s2)
    {
        int cnt=0;
        for (int i=0;i<s.length();i++)
        {
            if (s.charAt(i)!=s2.charAt(i))
                cnt+=1;
            if (cnt>1)
            return false;
        }
        return true;
    }
    public void go(String s,int cnt)
    {
        if (s.equals(t))
        {
            res=Math.min(res,cnt);
            return;
        }
        for (int i=0;i<w.length;i++)
        {
            if (visited[i]==0&&chk(s,w[i]))
            {
                visited[i]=1;
                go(w[i],cnt+1);
                visited[i]=0;
            }
        }
        
    }
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        t=target;
        w=words;
        go(begin,0);
        if (res==987654321)
            res=0;
        return res;
    }
}