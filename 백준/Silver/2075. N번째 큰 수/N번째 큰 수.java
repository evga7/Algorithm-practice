import java.io.*;
import java.util.*;

public class Main {
    static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N=Integer.parseInt(br.readLine());

        ArrayList<Integer> arr= new ArrayList<>();
        for (int i=0;i<N;i++){
            StringTokenizer st= new StringTokenizer(br.readLine());
            for (int j=0;j<N;j++) {
                arr.add(Integer.parseInt(st.nextToken()));
            }
        }
        Collections.sort(arr);
        bw.write(Integer.toString(arr.get((N*N)-N)));
        bw.flush();
    }
}