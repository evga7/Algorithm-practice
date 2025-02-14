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
    static int p[];
    public static int find(int x){
        if (x==p[x])
            return x;
        return p[x]=find(p[x]);
    }
    public static boolean uni(int x,int y){
        x=find(x);
        y=find(y);
        if (x!=y){
            if (x<y)
                p[y]=x;
            else
                p[x]=y;
            return true;
        }
        return false;
    }
    public static void main(String[] args) throws IOException{
        st=new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        int A,B;
        res=0;
        p=new int [N+1];
        for (int i=1;i<=N;i++)
            p[i]=i;
        boolean flag=false;
        for (int i=0;i<M;i++){
            st=new StringTokenizer(br.readLine());
            A=Integer.parseInt(st.nextToken());
            B=Integer.parseInt(st.nextToken());
            res+=1;
            if (uni(A,B)==false){
                flag=true;
                break;

            }

        }
        if (flag){
            bw.write(Integer.toString(res));
        }
        else{
            bw.write("0");
        }
        bw.flush();

    }
}