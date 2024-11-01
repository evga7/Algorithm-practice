import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static int res=0;
    static int N,K;
    static int arr[];
    static int dp[];
    static ArrayList<Integer> v=new ArrayList<>();
    public static int solve(int money){
        if (money==0)
            return 0;
        if (dp[money]!=-1)
            return dp[money];
        int ret=987654321;
        for (int i=0;i<N;i++){
            if (money-v.get(i)>=0){
                ret=Math.min(ret,solve(money-v.get(i))+1);
            }
        }
        dp[money]=ret;
        return dp[money];
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st =new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        K=Integer.parseInt(st.nextToken());
        dp=new int[K+1];
        Arrays.fill(dp,-1);
        for (int i=0;i<N;i++){
            int num=Integer.parseInt(br.readLine());
            v.add(num);
        }
        res=solve(K);
        if (res==987654321)
            res=-1;
        bw.write(Integer.toString(res));
        bw.close();

    }
}
