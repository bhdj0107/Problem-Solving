import java.io.*;
import java.util.*;

class Point {
    int x;
    int y;
    int delta;
    Point(int x, int y, int delta) {
        this.x = x;
        this.y = y;
        this.delta = delta;
    }

    public String toString() {
        return "(" + this.x + ", " + this.y + ", " + this.delta + ")";
    }
}

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        int field[][] = new int[N][N];
        Point shark = new Point(0, 0, 0);

        int sharkSize = 2;
        int eatCnt = 0;

        int totalMove = 0;

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int value = Integer.parseInt(st.nextToken());
                if (value == 9) { shark = new Point(j, i, 0); }
                else { field[i][j] = value; }
            }
        }

        while (true) {
            Point nextPoint = moveShark(field, shark, sharkSize);
            if (nextPoint.x != -1) {
                field[nextPoint.y][nextPoint.x] = 0;
                eatCnt += 1;
                totalMove += nextPoint.delta;
                if (eatCnt == sharkSize) {
                    eatCnt = 0;
                    sharkSize += 1;
                }
                shark = nextPoint;
            } else { break; }
        }

        System.out.println(totalMove);
    }

    static Point moveShark(int[][] field, Point shark, int sharkSize) {
        int dx[] = {0, -1, 0, 1}; int dy[] = {-1, 0, 1, 0};
        int N = field.length;
        Queue<Point> q = new LinkedList<>();
        Queue<Point> possibleFishes = new LinkedList<>();

        for (int i = 0; i < 4; i++) {
            int nx = shark.x + dx[i];
            int ny = shark.y + dy[i];
            if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                if (field[ny][nx] <= sharkSize)
                    q.add(new Point(nx, ny, 1));
            }
        }
        boolean visited[][] = new boolean[field.length][field.length];
        visited[shark.y][shark.x] = true;
        while (!q.isEmpty()) {
            Point now = q.remove();
            if (visited[now.y][now.x]) continue;
            else {
                visited[now.y][now.x] = true;
                if (field[now.y][now.x] < sharkSize && field[now.y][now.x] != 0) {
                    possibleFishes.add(now);
                }

                for (int i = 0; i < 4; i++) {
                    int nx = now.x + dx[i];
                    int ny = now.y + dy[i];
                    if (0 <= nx && nx < N && 0 <= ny && ny < N)
                        if (field[ny][nx] <= sharkSize)
                            q.add(new Point(nx, ny, now.delta + 1));
                }

            }
        }
        Point closestPoint = new Point(-1, -1, Integer.MAX_VALUE);
        if (possibleFishes.size() > 0) {
            while (!possibleFishes.isEmpty()) {
                Point p = possibleFishes.remove();
                if (p.delta < closestPoint.delta) closestPoint = p;
                else if (p.delta == closestPoint.delta) {
                    if (p.y < closestPoint.y) closestPoint = p;
                    else if (p.y == closestPoint.y) {
                        if (p.x < closestPoint.x) closestPoint = p;
                    }
                }
            }
        }
        return closestPoint;
    }
}