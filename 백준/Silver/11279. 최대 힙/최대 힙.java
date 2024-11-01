import java.io.*;
import java.util.*;

public class Main {
    static int res=0;
    static int N;
    static int c[][];
    static int arr[][];
    static PriorityQueue<Integer> pq= new PriorityQueue<>(Collections.reverseOrder());
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N=Integer.parseInt(br.readLine());
        for (int i=0;i<N;i++){
            int num=Integer.parseInt(br.readLine());
            if (num==0){
                if (pq.isEmpty())
                    bw.write("0\n");
                else
                    bw.write(Integer.toString(pq.poll())+"\n");
            }
            else
                pq.add(num);
        }
        bw.close();

    }
}
