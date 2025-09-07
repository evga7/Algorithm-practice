import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int N,M,res;
    static int p[];
    public static int find(int x){
        if (p[x]==x)
            return x;
        p[x]=find(p[x]);
        return p[x];
    }
    public static boolean uni(int x,int y){
        x=find(x);
        y=find(y);
        if (x!=y)
        {
            if (x<y)
                p[x]=y;
            else
                p[y]=x;
            return true;
        }
        return false;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw =new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        N=Integer.parseInt(br.readLine());
        M=Integer.parseInt(br.readLine());
        int A,B;
        p= new int [N+1];
        for (int i=1;i<=N;i++)
            p[i]=i;
        for (int i=0;i<M;i++){
            st= new StringTokenizer(br.readLine());
            A=Integer.parseInt(st.nextToken());
            B=Integer.parseInt(st.nextToken());
            uni(A,B);
        }
        int num=find(1);
        for (int i=2;i<=N;i++){
            if (num==find(i))
                res+=1;
        }
        bw.write(Integer.toString(res));
        bw.close();

    }


}
