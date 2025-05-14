import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] first = br.readLine().split(" ");
        int N = Integer.parseInt(first[0]);
        int K = Integer.parseInt(first[1]);
        int M = Integer.parseInt(first[2]);

        int[] L = new int[N];
        for (int i = 0; i < N; i++) {
            L[i] = Integer.parseInt(br.readLine());
        }

        int left = 1, right = 1_000_000_000;
        int answer = -1;

        // 이진 탐색: P = mid 로 잘랐을 때 조각 개수 cnt 계산
        while (left <= right) {
            int mid = left + (right - left) / 2;
            long cnt = 0;
            long twoK = 2L * K;

            for (int cur : L) {
                if (cur <= K) continue;    // 꼬다리 한 번도 못 자르면 폐기
                long s = cur;
                if (twoK <= cur) s -= twoK; // 양쪽에서 K씩 자름
                else s -= K;                // 한쪽만 자름
                if (s > 0) cnt += s / mid;  // 남은 길이로 조각 개수 계산
            }

            if (cnt >= M) {
                answer = mid;       // 가능한 경우, 더 큰 P 탐색
                left = mid + 1;
            } else {
                right = mid - 1;    // 불가능하면 P를 줄임
            }
        }

        System.out.println(answer);
    }
}
