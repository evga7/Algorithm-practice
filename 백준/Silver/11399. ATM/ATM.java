import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        int[] a = new int[N];
        
        String[] input = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            a[i] = Integer.parseInt(input[i]);
        }
        
        Arrays.sort(a);
        
        long res = 0;
        long c = 0;
        for (int cur : a) {
            c += cur;
            res += c;
        }
        
        System.out.println(res);
    }
}
