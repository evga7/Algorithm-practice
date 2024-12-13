import java.io.*;
import java.util.*;

public class Main {


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N=Integer.parseInt(br.readLine());
        TreeMap<String,Integer> m =new TreeMap<>();
        for (int i=0;i<N;i++){
            StringTokenizer st= new StringTokenizer(br.readLine(),".");
            st.nextToken();
            String temp=st.nextToken();
            m.put(temp,m.getOrDefault(temp,0)+1);
        }
        for (String cur : m.keySet()){
            bw.write(cur+" "+Integer.toString(m.get(cur))+"\n");
        }
        bw.close();

    }
}
