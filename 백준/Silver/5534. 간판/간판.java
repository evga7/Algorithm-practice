import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String pattern = br.readLine();
        int count = 0;

        for (int i = 0; i < N; i++) {
            String t = br.readLine();
            if (matchesPattern(t, pattern)) {
                count++;
            }
        }

        System.out.println(count);
    }

    private static boolean matchesPattern(String t, String s) {
        // 1) 접두사로 바로 포함되는 경우
        if (t.startsWith(s)) {
            return true;
        }
        // 2) 길이가 더 짧으면 불가능
        if (t.length() < s.length()) {
            return false;
        }
        // 3) 등차 간격으로 찾아보기
        int n = t.length(), m = s.length();
        for (int i = 0; i < n; i++) {
            if (t.charAt(i) != s.charAt(0)) continue;
            // j = 간격 (1부터 99까지)
            for (int j = 1; j < 100; j++) {
                int idx = 1;
                for (int k = i + j; k < n; k += j) {
                    if (t.charAt(k) != s.charAt(idx)) {
                        break;
                    }
                    idx++;
                    if (idx == m) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}
