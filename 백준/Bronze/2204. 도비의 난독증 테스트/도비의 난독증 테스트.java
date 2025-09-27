import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static int N,M,res;
    static int p[];

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw =new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<String> arr= new ArrayList<>();
        while (true) {
            N = Integer.parseInt(br.readLine());
            arr.clear();
            if (N == 0)
                break;
            for (int i = 0; i < N; i++)
                arr.add(br.readLine());
            Collections.sort(arr,String.CASE_INSENSITIVE_ORDER);
            bw.write(arr.get(0)+"\n");
        }
        bw.close();

    }


}
