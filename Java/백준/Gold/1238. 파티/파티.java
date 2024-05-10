import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int INF = Integer.MAX_VALUE / 2 - 2;
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken()) - 1;

        int[][] dist = new int[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken());
            int dst = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            dist[src - 1][dst - 1] = d;
        }

        for (int k = 0; k < N; k++) {
            for (int a = 0; a < N; a++) {
                for (int b = 0; b < N; b++) {
                    dist[a][b] = Integer.min(dist[a][b], dist[a][k] + dist[k][b]);
                }
            }
        }
        
        int maxDist = -1;
        for (int i = 0; i < N; i++) {
            int nowDist = dist[i][X] + dist[X][i];
            if (nowDist > maxDist) maxDist = nowDist;
        }
        System.out.println(maxDist);

    }
}