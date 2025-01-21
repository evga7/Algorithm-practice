import java.io.*;
import java.util.*;

public class Main {
    static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N=Integer.parseInt(br.readLine());
        StringTokenizer st= new StringTokenizer(br.readLine());
        HashSet<Integer> st2=new HashSet<>();
        for (int i=0;i<N;i++){
            st2.add(Integer.parseInt(st.nextToken()));
        }
        N=Integer.parseInt(br.readLine());
        st= new StringTokenizer(br.readLine());
        for (int i=0;i<N;i++){
            int num=Integer.parseInt(st.nextToken());
            if (st2.contains(num)==true){
                bw.write("1 ");
            }
            else
                bw.write("0 ");
        }
        bw.flush();
    }
}