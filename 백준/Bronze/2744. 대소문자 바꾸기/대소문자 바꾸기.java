import java.io.*;
import java.lang.reflect.Array;
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
        String s=st.nextToken();
        StringBuilder sb=new StringBuilder();
        for (int i=0;i<s.length();i++) {
            if (Character.isUpperCase(s.charAt(i)))
                sb.append(Character.toLowerCase(s.charAt(i)));
            else
                sb.append(Character.toUpperCase(s.charAt(i)));
        }
        bw.write(sb.toString());
        bw.flush();



    }
}