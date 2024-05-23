import java.io.*;
import java.util.*;


public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        byte box[][] = new byte[N][M];
        boolean[][] visited = new boolean[N][M];

        int nonTomatoCnt = 0;
        Queue<int[]> q = new LinkedList<>();


        for (int j = 0; j < N; j++) {
            st = new StringTokenizer(br.readLine());
            for (int k = 0; k < M; k++) {
                int tomato = Integer.parseInt(st.nextToken());
                if (tomato == -1) {
                    box[j][k] = -1;
                } else if (tomato == 0) {
                    box[j][k] = 0;
                    nonTomatoCnt += 1;
                } else if (tomato == 1) {
                    box[j][k] = 1;
                    nonTomatoCnt += 1;
                    q.add(new int[]{j, k, 0});
                }
            }
        }


        byte[] dx = {1, -1, 0, 0};
        byte[] dy = {0, 0, 1, -1};

        int ans = -1;
        while (!q.isEmpty()) {
            int[] thisPosition = q.remove();
            int y = thisPosition[0];
            int x = thisPosition[1];
            int dist = thisPosition[2];

            if (visited[y][x]) continue;
            else {
                visited[y][x] = true;
                nonTomatoCnt -= 1;

                if (nonTomatoCnt == 0) {
                    ans = dist;
                    break;
                }
                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (0 > nx || nx >= M) continue;
                    if (0 > ny || ny >= N) continue;
                    if (box[ny][nx] == 0) {
                        q.add(new int[]{ny, nx, dist + 1});
                    }
                }
            }
        }
        
        System.out.println(ans);
    }
}