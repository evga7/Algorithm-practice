import java.io.*;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int []dx={-1,0,1,0};
    static int [] dy={0,1,0,-1};
    static int N;
    static int M;
    static boolean is_inside(int x,int y,int N,int M)
    {
        return 0<=x&&x<N &&0<=y&&y<M;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        HashMap<String, Integer> m = new HashMap<>();
        HashMap<Integer,String> m2 = new HashMap<>();
        for (int i=0;i<N;i++) {
            String s = br.readLine();
            m.put(s,i+1);
            m2.put(i+1,s);
        }
        for (int i=0;i<M;i++)
        {
            String s = br.readLine();
            if (Character.isDigit(s.charAt(0)))
            {
                int ss=Integer.parseInt(s);
                bw.write(m2.get(ss)+"\n");
            }
            else
            {
                bw.write(m.get(s)+"\n");
            }
        }
        bw.flush();

    }


}