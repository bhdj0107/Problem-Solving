import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        // 0-1 BFS
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Deque<int[]> dq = new LinkedList<>();
        boolean[] visited = new boolean[200001];
        int[] dist = new int[200001];

        dist[N] = 0;
        
        dq.addFirst(new int[]{N, 0});

        while (!dq.isEmpty()) {
            int[] poppedArray = dq.pollFirst();
            int popped = poppedArray[0];
            int tDist = poppedArray[1];

            if (visited[popped]) continue;
            visited[popped] = true;
            dist[popped] = tDist;
            if (popped * 2 <= 200000) {
                dq.addFirst(new int[]{popped * 2, tDist});
            }
            if (popped - 1 >= 0) {
                dq.addLast(new int[]{popped - 1, tDist + 1});
            }
            if (popped + 1 <= 200000) {
                dq.addLast(new int[]{popped + 1, tDist + 1});
            }
        }
        System.out.println(dist[M]);
    }
}