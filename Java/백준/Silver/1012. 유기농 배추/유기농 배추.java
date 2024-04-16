import java.io.*;
import java.util.*;

class Point {
    public int x;
    public int y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            boolean field[][] = new boolean[N][M];
            
            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                field[y][x] = true;
            }

            Queue<Point> q = new LinkedList<>();
            boolean visited[][] = new boolean[N][M];
            int dx[] = {-1, 0, 1, 0};
            int dy[] = {0, -1, 0, 1};
            int unionCnt = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (!visited[i][j]) {
                        if (field[i][j]) {
                            unionCnt += 1;
                            q.add(new Point(j, i));
                            while (!q.isEmpty()) {
                                Point now = q.remove();
                                if (visited[now.y][now.x]) continue;
                                visited[now.y][now.x] = true;
                                for (int k = 0; k < 4; k++) {
                                    int ny = now.y + dy[k];
                                    int nx = now.x + dx[k];
                                    if (0 <= nx && nx < M && 0 <= ny && ny < N) {
                                        if (field[ny][nx]) q.add(new Point(nx, ny));
                                    }
                                }
                            }
                        }
                    }
                }
            }
            System.out.println(unionCnt);
        }
    }
}