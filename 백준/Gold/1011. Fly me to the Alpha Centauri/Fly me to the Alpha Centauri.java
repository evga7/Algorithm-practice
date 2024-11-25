import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static int solve(int N){
        int speed=0;
        int k=1;
        int res=0;
        while (N>0) {
            if (N-(speed+k)<=0){
                res+=1;
                break;
            }
            res+=2;
            speed+=k;
            N-=speed*2;
        }
        return res;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T;
        T=Integer.parseInt(br.readLine());

        while (T>0){
            T-=1;
            int A,B;
            StringTokenizer st= new StringTokenizer(br.readLine());
            A=Integer.parseInt(st.nextToken());
            B=Integer.parseInt(st.nextToken());
            int pos=B-A;
            bw.write(solve(pos)+"\n");
        }
        bw.close();
    }
}
