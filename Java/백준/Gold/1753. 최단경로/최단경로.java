import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int INF = Integer.MAX_VALUE / 2 - 2;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(br.readLine()) - 1;

        HashMap<Integer,Integer>[] edges = new HashMap[V];
        for (int i = 0; i < V; i++) edges[i] = new HashMap<>();
        
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken()) - 1;
            int dst = Integer.parseInt(st.nextToken()) - 1;
            int amount = Integer.parseInt(st.nextToken());

            if (edges[src].containsKey(dst)) {
                if (edges[src].get(dst) > amount) edges[src].put(dst, amount);
            } else edges[src].put(dst, amount);
        }

        int[] dist = new int[V];
        boolean[] visited = new boolean[V];

        Arrays.fill(dist, INF);
        dist[S] = 0;
        for (int i = 0; i < V; i++) {
            // pick closest vertex
            int minV = -1;
            int minDist = Integer.MAX_VALUE;

            for (int j = 0; j < V; j++) {
                if (visited[j]) continue;
                if (minDist > dist[j]) {
                    minDist = dist[j];
                    minV = j;
                }
            }
            visited[minV] = true;
            for (int next : edges[minV].keySet()) {
                dist[next] = Integer.min(dist[next], dist[minV] + edges[minV].get(next));
            }
        }

        for (int i = 0; i < V; i++) {
            bw.write((dist[i] != INF)?Integer.toString(dist[i]):"INF");
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }

}
