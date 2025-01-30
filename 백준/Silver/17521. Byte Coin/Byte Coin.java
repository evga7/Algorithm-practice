import java.io.*;
import java.util.*;

public class Main {
    static long N,M;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st= new StringTokenizer(br.readLine());
        N=Long.parseLong(st.nextToken());
        M=Long.parseLong(st.nextToken());
        long cnt=0;
        long mi=987654321;
        long mx=0;
        for (int i=0;i<N;i++){
            int num=Integer.parseInt(br.readLine());
            if (mi>num || mx>num){
                M+=cnt*mx;
                cnt=M/num;
                M-=cnt*num;
                mi=num;
                mx=num;
                continue;
            }
            mx=Math.max(mx,num);
        }
        M+=cnt*mx;
        bw.write(Long.toString(M));
        bw.flush();
    }
}