import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        int right=0;
        long s=0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long S=Long.parseLong(st.nextToken());
        long res=1;
        while (true)
        {
            right+=1;
            if (s+right>S){
                break;
            }
            s+=right;
        }
        bw.write(String.valueOf(right-1));
        bw.flush();
    }


}