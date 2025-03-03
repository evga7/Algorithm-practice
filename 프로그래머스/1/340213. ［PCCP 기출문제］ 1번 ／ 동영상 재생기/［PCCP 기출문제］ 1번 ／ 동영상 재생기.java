class Solution {
    public static int conv(String s){
        String arr[]=s.split(":");
        int M,S;
        M=Integer.parseInt(arr[0]);
        S=Integer.parseInt(arr[1]);
        return M*60+S;
    }
    public static String conv2(int s){
        int M,S;
        M=s/60;
        S=s%60;
        String mm;
        String ss;
        mm=Integer.toString(M);
        ss=Integer.toString(S);
        if (M<10)
            mm="0"+mm;
        if (S<10)
            ss="0"+ss;
        
        return mm+":"+ss;
    }
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = "";
        int len=conv(video_len);
        int cur=conv(pos);
        int o_start=conv(op_start);
        int o_end=conv(op_end);
        for (int i=0;i<commands.length;i++){
            String op=commands[i];
            if (o_start<=cur&& cur<=o_end){
                cur=o_end;
            }
            if (op.equals("next")){
                cur=Math.min(cur+10,len);
            }
            else{
                cur=Math.max(cur-10,0);
            }
        }
            if (o_start<=cur&& cur<=o_end){
                cur=o_end;
            }
        return conv2(cur);
    }
}