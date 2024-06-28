import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {

    static int[] dp=new int[1000001];
    static boolean visited[];
    static int N;
    public static int solve(int num){
        if (num==1)
            return 0;
        if (dp[num]!=-1)
            return dp[num];
        int ret=987654321;
        if (num%3==0)
            ret=Math.min(ret,solve(num/3)+1);
        if (num%2==0)
            ret=Math.min(ret,solve(num/2)+1);
        ret=Math.min(ret,solve(num-1)+1);
        dp[num]=ret;
        return dp[num];

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        Arrays.fill(dp,-1);
        System.out.println(solve(N));

    }
}