import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int INF = Integer.MAX_VALUE / 2 - 2;
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        int[][] dist = new int[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }

        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken());
            int dst = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            dist[src - 1][dst - 1] = Integer.min(dist[src-1][dst-1], d);
        }

        for (int k = 0; k < N; k++) {
            for (int a = 0; a < N; a++) {
                for (int b = 0; b < N; b++) {
                    dist[a][b] = Integer.min(dist[a][b], dist[a][k] + dist[k][b]);
                }
            }
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N - 1; j++) {
                if (dist[i][j] != INF) bw.write(Integer.toString(dist[i][j]) + " ");
                else bw.write("0 ");
            }
            if (dist[i][N - 1] != INF) bw.write(Integer.toString(dist[i][N - 1]) + "\n");
            else bw.write("0\n");
        }

        bw.flush();
        bw.close();

    }
}