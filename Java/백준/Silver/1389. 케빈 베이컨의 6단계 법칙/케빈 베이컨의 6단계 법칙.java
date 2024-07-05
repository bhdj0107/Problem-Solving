import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static HashMap<Integer, HashSet<Integer>> connection = new HashMap<>();
    static int[][] dist;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        visited = new boolean[N + 1];
        dist = new int[N + 1][N + 1];
        for (int i = 1; i < N + 1; i++) {
            connection.put(i, new HashSet<Integer>());
            Arrays.fill(dist[i], -1);
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            dist[a][b] = 1;
            dist[b][a] = 1;
            connection.get(a).add(b);
            connection.get(b).add(a);
        }

        int[] baconNumbers = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            int thisBacon = 0;
            for (int j = 1; j < N + 1; j++) {
                if (i == j) continue;
                thisBacon += getMinimumDistance(i, j);
            }
            baconNumbers[i] = thisBacon;
        }
        int ans = -1;
        int ansmin = Integer.MAX_VALUE;

        for (int i = 1; i < N + 1; i++) {
            if (ansmin > baconNumbers[i]) {
                ansmin = baconNumbers[i];
                ans = i;
            }
        }

        System.out.println(ans);

    }

    static int getMinimumDistance(int src, int dst) {
        if (dist[src][dst] != -1) return dist[src][dst];
        else {
            int min = Integer.MAX_VALUE - 200;
            visited[src] = true;
            for (int t : connection.get(src)) {
                if (visited[t]) continue;
                int tDist = getMinimumDistance(t, dst) + 1;
                min = Integer.min(min, tDist);
            }
            visited[src] = false;
            if (min != Integer.MAX_VALUE - 200) {
                dist[src][dst] = min;
                dist[dst][src] = min;
            }
            return min;
        }
    }
}