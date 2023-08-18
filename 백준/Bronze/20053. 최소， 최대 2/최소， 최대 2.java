import java.io.*;
import java.util.*;

public class Main {
    static int []dx={-1,0,1,0};
    static int [] dy={0,1,0,-1};
    static int N,M,T;
    static int arr[];
    static int visited[];
    static Vector<Integer> v= new Vector<Integer>();
    static BufferedReader br;
    static BufferedWriter bw;
    static StringTokenizer st;
    static boolean is_inside(int x,int y,int N,int M)
    {
        return 0<=x&&x<N &&0<=y&&y<M;
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st = new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        while (N>0) {
            N-=1;
            st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            int res_min = 1000001;
            int res_max = -1000001;
            st = new StringTokenizer(br.readLine());
            for (int i=0;i<M;i++)
            {
                int num= Integer.parseInt(st.nextToken());
                res_min=Math.min(res_min,num);
                res_max=Math.max(res_max,num);
            }
            bw.write(Integer.toString(res_min)+' '+Integer.toString(res_max)+"\n");
        }

        bw.flush();
    }
}