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

    static void go(int idx,int cnt) throws IOException {
        if (cnt==M)
        {
            for (int i=0;i<M;i++)
                bw.write(String.valueOf(v.get(i)+" "));
            bw.write("\n");
            return;
        }
        int back=-1;
        for (int i=idx;i<N;i++)
        {
            if (visited[i]==0 && back!=arr[i]) {
                visited[i]=1;
                v.add(arr[i]);
                back=arr[i];
                go(i + 1, cnt + 1);
                v.remove(v.size() - 1);
                visited[i]=0;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st = new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        arr=new int[N];
        visited=new int[N];
        st=new StringTokenizer(br.readLine());
        for (int i=0;i<N;i++)
        {
            int num=Integer.parseInt(st.nextToken());
            arr[i]=num;
        }
        Arrays.sort(arr);
        go(0,0);
        bw.flush();
    }
}