import java.io.*;
import java.util.*;


public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());

        byte box[][][] = new byte[H][N][M];
        boolean[][][] visited = new boolean[H][N][M];

        int nonTomatoCnt = 0;
        Queue<int[]> q = new LinkedList<>();

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < M; k++) {
                    int tomato = Integer.parseInt(st.nextToken());
                    if (tomato == -1) {
                        box[i][j][k] = -1;
                    } else if (tomato == 0) {
                        box[i][j][k] = 0;
                        nonTomatoCnt += 1;
                    } else if (tomato == 1) {
                        box[i][j][k] = 1;
                        nonTomatoCnt += 1;
                        q.add(new int[]{i, j, k, 0});
                    }
                }
            }
        }

        byte[] dx = {1, -1, 0, 0, 0, 0};
        byte[] dy = {0, 0, 1, -1, 0, 0};
        byte[] dz = {0, 0, 0, 0, 1, -1};

        int ans = -1;
        while (!q.isEmpty()) {
            int[] thisPosition = q.remove();
            int z = thisPosition[0];
            int y = thisPosition[1];
            int x = thisPosition[2];
            int dist = thisPosition[3];

            if (visited[z][y][x]) continue;
            else {
                visited[z][y][x] = true;
                nonTomatoCnt -= 1;

                if (nonTomatoCnt == 0) {
                    ans = dist;
                    break;
                }
                for (int i = 0; i < 6; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    int nz = z + dz[i];

                    if (0 > nx || nx >= M) continue;
                    if (0 > ny || ny >= N) continue;
                    if (0 > nz || nz >= H) continue;
                    if (box[nz][ny][nx] == 0) {
                        q.add(new int[]{nz, ny, nx, dist + 1});
                    }
                }
            }
        }
        
        System.out.println(ans);
    }
}