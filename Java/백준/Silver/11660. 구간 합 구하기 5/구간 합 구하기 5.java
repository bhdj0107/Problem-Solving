import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Queue<int[]> q = new LinkedList<>();
        int maxX = -1;
        int maxY = -1;
        int[][] map = new int[N + 1][N + 1];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) map[i + 1][j + 1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int[] t = new int[4];
            t[0] = Integer.parseInt(st.nextToken());
            t[1] = Integer.parseInt(st.nextToken());
            t[2] = Integer.parseInt(st.nextToken());
            t[3] = Integer.parseInt(st.nextToken());
            q.add(t);
            if (maxY < t[2]) maxY = t[2];
            if (maxX < t[3]) maxX = t[3];
        }

        for (int i = 1; i < N + 1; i++) {
            map[i][1] += map[i - 1][1];
            map[1][i] += map[1][i - 1];
        }
        
        for (int i = 2; i < maxY + 1; i++) {
            for (int j = 2; j < maxX + 1; j++) {
                map[i][j] += (map[i-1][j] + map[i][j-1] - map[i - 1][j - 1]);
            }
        }

        while (!q.isEmpty()) {
            int[] t = q.remove();
            int y1 = t[0] - 1;
            int x1 = t[1] - 1;
            int y2 = t[2];
            int x2 = t[3];
            
            int ans = map[y2][x2] - map[y2][x1] - map[y1][x2] + map[y1][x1];
            bw.write(ans + "\n");
        }
        bw.flush();
        bw.close();
    }

}
