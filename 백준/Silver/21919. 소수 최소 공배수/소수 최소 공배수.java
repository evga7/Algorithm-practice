import java.io.*;
import java.util.*;

public class Main {
    static int N,M;
    static int res;
    static boolean visited[];
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    static int dx[]={1,0,-1,0};
    static int dy[]={0,1,0,-1};
    static int dp[][];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static boolean p[]=new boolean [1000001];

    static void go(){
        for (int i=2;i<=Math.sqrt(1000000);i++){
            if (p[i]==true)continue;
            for (int j=i*i;j<=1000000;j+=i){
                p[j]=true;
            }
        }
    }
    static long gcd(long a,long b){
        long temp;
        while (b>0){
            temp=a%b;
            a=b;
            b=temp;
        }
        return a;
    }
    public static void main(String[] args) throws IOException{

        N=Integer.parseInt(br.readLine());
        int num;
        long res=1;
        st=new StringTokenizer(br.readLine());
        go();
        p[1]=p[0]=true;
        for (int i=0;i<N;i++){
            num=Integer.parseInt(st.nextToken());
            if (p[num]==false) {
                res=(res*num)/gcd(res,num);
            }
        }
        if (res==1)
            bw.write("-1");
        else
            bw.write(Long.toString(res));
        bw.flush();
    }
}