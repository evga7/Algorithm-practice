import java.io.*;
import java.util.*;

public class Main {


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st= new StringTokenizer(br.readLine());
        int N,M;
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        TreeMap<String,Integer> m= new TreeMap<>();
        for (int i=0;i<N+M;i++){
            String temp=br.readLine();
            m.put(temp,m.getOrDefault(temp,0)+1);
        }
        int res=0;
        List<String > arr= new ArrayList<>();
        for (String cur :m.keySet()){
            if (m.get(cur)==2){
                arr.add(cur);
            }
        }
        bw.write(Integer.toString(arr.size())+"\n");
        for (String cur :arr){
            bw.write(cur+"\n");
        }
        bw.close();

    }
}
