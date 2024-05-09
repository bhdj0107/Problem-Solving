import java.io.*;
import java.util.*;

class Point {
    public int x;
    public int y;
    public boolean isBroke;
    public int delta;
    Point (int x, int y, boolean isBroke, int delta) {
        this.x = x;
        this.y = y;
        this.isBroke = isBroke;
        this.delta = delta;
    }
}
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] field = new int[N][M];
        for (int i = 0; i < N; i++) {
            String inp = br.readLine();
            for (int j = 0; j < M; j++) {
                field[i][j] = Integer.parseInt(inp.substring(j, j + 1));
            }
        }

        Queue<Point> q = new LinkedList<>();
        boolean[][][] isVisited = new boolean[2][N][M];
        q.add(new Point(0, 0, false, 0));
        isVisited[0][0][0] = false;
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};

        int reach = -1;

        while (!q.isEmpty()) {
            Point now = q.remove();
            int isBroken = now.isBroke?1:0;

            if (now.x == M - 1 && now.y == N - 1) {
                reach = now.delta + 1;
                break;
            }

            if (isVisited[isBroken][now.y][now.x]) continue;
            isVisited[isBroken][now.y][now.x] = true;
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                if (0 <= nx && nx < M && 0 <= ny && ny < N) {
                    if (isBroken == 1) {
                        if (field[ny][nx] == 0) q.add(new Point(nx, ny, true, now.delta + 1));
                    } else {
                        if (field[ny][nx] == 0) q.add(new Point(nx, ny, false, now.delta + 1));
                        else q.add(new Point(nx, ny, true, now.delta + 1));
                    }
                }
            }
        }

        System.out.println(reach);

    }
}