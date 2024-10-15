class Solution {
    public String solution(String s) {
        String answer = "";
        String t[] = s.split(" ");
        int mx=-987654321;
        int mi=987654321;
        for (String cur : t)
        {
            int a=Integer.parseInt(cur);
            mx=Math.max(mx,a);
            mi=Math.min(mi,a);
        }
        return mi+" "+mx;
    }
}