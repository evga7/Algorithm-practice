import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        StringTokenizer num= new StringTokenizer(br.readLine());
        int[] arr=new int[N+1];
        int s=-101;
        for (int i=1;i<=N;i++)
        {
            arr[i]=Integer.parseInt(num.nextToken());
            arr[i]+=arr[i-1];
        }
        for (int i=M;i<=N;i++)
        {
            s=Math.max(s,arr[i]-arr[i-M]);
        }
        bw.write(String.valueOf(s));
        bw.flush();
    }


}