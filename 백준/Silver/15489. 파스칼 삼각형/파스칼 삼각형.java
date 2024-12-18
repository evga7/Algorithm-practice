import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st= new StringTokenizer(br.readLine());
        int R,C,W;

        R=Integer.parseInt(st.nextToken());
        C=Integer.parseInt(st.nextToken());
        W=Integer.parseInt(st.nextToken());
        int arr[][]=new int[33][33];
        arr[1][1]=1;
        for (int i=1;i<=30;i++){
            for (int j=1;j<=i;j++){
                arr[i][j]+=arr[i-1][j]+arr[i-1][j-1];
            }
        }
        int res=0;
        int idx=0;
        for (int i=R;i<R+W;i++){
            idx+=1;
            for (int j=C;j<C+idx;j++){
                res+=arr[i][j];
            }
        }
        bw.write(Integer.toString(res));
        bw.close();

    }
}
