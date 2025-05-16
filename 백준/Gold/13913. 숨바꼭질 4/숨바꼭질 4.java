import java.io.*;
import java.util.*;

public class Main {
    static final int MAX = 100001;
    static int[] parent = new int[MAX];
    static boolean[] visited = new boolean[MAX];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        bfs(N, M);

        // 시간 출력
        List<Integer> path = new ArrayList<>();
        int cur = M;
        while (cur != N) {
            path.add(cur);
            cur = parent[cur];
        }
        path.add(N);
        Collections.reverse(path);

        System.out.println(path.size() - 1);
        for (int p : path) {
            System.out.print(p + " ");
        }
    }

    static void bfs(int start, int target) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int cur = queue.poll();
            if (cur == target) break;

            for (int next : new int[]{cur - 1, cur + 1, cur * 2}) {
                if (next >= 0 && next < MAX && !visited[next]) {
                    visited[next] = true;
                    parent[next] = cur;
                    queue.offer(next);
                }
            }
        }
    }
}
