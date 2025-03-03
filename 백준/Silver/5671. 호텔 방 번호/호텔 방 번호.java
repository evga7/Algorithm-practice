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
    static ArrayList<Integer> arr= new ArrayList<>();
    static StringTokenizer st;
    static int p[];
    static int d[];
    public Set<Integer> st2 =new HashSet<>();
    public static void go(){
        for (int i=1;i<=5000;i++){
            int c []=new int [10];
            String cur=Integer.toString(i);
            boolean flag=true;
            for (int j=0;j<cur.length();j++){
                int cur2=cur.charAt(j)-'0';
                if (c[cur2]==1)
                {
                    flag=false;
                    break;
                }
                c[cur2]=1;
            }
            if (flag==false){
                d[i]=0;
            }

        }

    }
    public static void main(String[] args) throws IOException {
        d = new int [5001];
            for (int i=1;i<=5000;i++){
                d[i]=1;
            }
        go();
        for (int i=1;i<=5000;i++){
            d[i]+=d[i-1];
        }
        String s;
        while ((s=br.readLine())!=null){
            st=new StringTokenizer(s);
            N=Integer.parseInt(st.nextToken());
            M=Integer.parseInt(st.nextToken());
            bw.write(Integer.toString(d[M]-d[N-1])+"\n");
        }
        bw.flush();

    }


}